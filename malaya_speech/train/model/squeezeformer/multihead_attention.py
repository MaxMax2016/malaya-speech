# Copyright 2020 Huy Le Nguyen (@usimarit)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import typing
import tensorflow as tf

from ..utils import shape_list

logger = tf.get_logger()


class MultiHeadAttention(tf.keras.layers.Layer):
    def __init__(
        self,
        num_heads,
        head_size,
        output_size: int = None,
        dropout: float = 0.0,
        use_projection_bias: bool = True,
        return_attn_coef: bool = False,
        **kwargs,
    ):
        super(MultiHeadAttention, self).__init__(**kwargs)

        if output_size is not None and output_size < 1:
            raise ValueError("output_size must be a positive number")

        self.head_size = head_size
        self.num_heads = num_heads
        self.output_size = output_size
        self.use_projection_bias = use_projection_bias
        self.return_attn_coef = return_attn_coef

        self.dropout = tf.keras.layers.Dropout(dropout, name="dropout")
        self._droput_rate = dropout

    def build(self, input_shape):
        num_query_features = input_shape[0][-1]
        num_key_features = input_shape[1][-1]
        num_value_features = (
            input_shape[2][-1] if len(input_shape) > 2 else num_key_features
        )
        output_size = (
            self.output_size if self.output_size is not None else num_value_features
        )
        input_max = (self.num_heads * self.head_size) ** -0.5
        self.query = tf.keras.layers.Dense(
            self.num_heads * self.head_size, activation=None,
            kernel_initializer=tf.keras.initializers.RandomUniform(minval=-input_max, maxval=input_max),
            bias_initializer=tf.keras.initializers.RandomUniform(minval=-input_max, maxval=input_max),
        )
        self.key = tf.keras.layers.Dense(
            self.num_heads * self.head_size, activation=None,
            kernel_initializer=tf.keras.initializers.RandomUniform(minval=-input_max, maxval=input_max),
            bias_initializer=tf.keras.initializers.RandomUniform(minval=-input_max, maxval=input_max),
        )
        self.value = tf.keras.layers.Dense(
            self.num_heads * self.head_size, activation=None,
            kernel_initializer=tf.keras.initializers.RandomUniform(minval=-input_max, maxval=input_max),
            bias_initializer=tf.keras.initializers.RandomUniform(minval=-input_max, maxval=input_max),
        )
        self.projection_kernel = self.add_weight(
            name="projection_kernel",
            shape=[self.num_heads, self.head_size, output_size],
            initializer=tf.keras.initializers.RandomUniform(minval=-input_max, maxval=input_max),
        )
        if self.use_projection_bias:
            self.projection_bias = self.add_weight(
                name="projection_bias",
                shape=[output_size],
                initializer=tf.keras.initializers.RandomUniform(minval=-input_max, maxval=input_max),
            )
        else:
            self.projection_bias = None

    def call_qkv(self, query, key, value, training=False):
        # verify shapes
        if key.shape[-2] != value.shape[-2]:
            raise ValueError(
                "the number of elements in 'key' must be equal to "
                "the same as the number of elements in 'value'"
            )
        # Linear transformations
        query = self.query(query)
        B, T, E = shape_list(query)
        query = tf.reshape(query, [B, T, self.num_heads, self.head_size])

        key = self.key(key)
        B, T, E = shape_list(key)
        key = tf.reshape(key, [B, T, self.num_heads, self.head_size])

        value = self.value(value)
        B, T, E = shape_list(value)
        value = tf.reshape(value, [B, T, self.num_heads, self.head_size])

        return query, key, value

    def call_attention(self, query, key, value, logits, training=False, mask=None):
        # mask = attention mask with shape [B, Tquery, Tkey] with 1 is for positions we want to attend, 0 for masked
        if mask is not None:
            if len(mask.shape) < 2:
                raise ValueError("'mask' must have at least 2 dimensions")
            if query.shape[-3] != mask.shape[-2]:
                raise ValueError(
                    "mask's second to last dimension must be equal to "
                    "the number of elements in 'query'"
                )
            if key.shape[-3] != mask.shape[-1]:
                raise ValueError(
                    "mask's last dimension must be equal to the number of elements in 'key'"
                )
        # apply mask
        if mask is not None:
            mask = tf.cast(mask, tf.float32)

            # possibly expand on the head dimension so broadcasting works
            if len(mask.shape) != len(logits.shape):
                mask = tf.expand_dims(mask, -3)

            logits += -10e9 * (1.0 - mask)

        attn_coef = tf.nn.softmax(logits)

        # attention dropout
        attn_coef_dropout = self.dropout(attn_coef, training=training)

        # attention * value
        multihead_output = tf.einsum("...HNM,...MHI->...NHI", attn_coef_dropout, value)

        # Run the outputs through another linear projection layer. Recombining heads
        # is automatically done.
        output = tf.einsum("...NHI,HIO->...NO", multihead_output, self.projection_kernel)

        if self.projection_bias is not None:
            output += self.projection_bias

        return output, attn_coef

    def call(self, inputs, training=False, mask=None, **kwargs):
        query, key, value = inputs

        query, key, value = self.call_qkv(query, key, value, training=training)

        # Scale dot-product, doing the division to either query or key
        # instead of their product saves some computation
        depth = tf.constant(self.head_size, dtype=tf.float32)
        query /= tf.sqrt(depth)

        # Calculate dot product attention
        logits = tf.einsum("...NHO,...MHO->...HNM", query, key)

        output, attn_coef = self.call_attention(query, key, value, logits,
                                                training=training, mask=mask)

        if self.return_attn_coef:
            return output, attn_coef
        else:
            return output

    def compute_output_shape(self, input_shape):
        num_value_features = (
            input_shape[2][-1] if len(input_shape) > 2 else input_shape[1][-1]
        )
        output_size = (
            self.output_size if self.output_size is not None else num_value_features
        )

        output_shape = input_shape[0][:-1] + (output_size,)

        if self.return_attn_coef:
            num_query_elements = input_shape[0][-2]
            num_key_elements = input_shape[1][-2]
            attn_coef_shape = input_shape[0][:-2] + (
                self.num_heads,
                num_query_elements,
                num_key_elements,
            )

            return output_shape, attn_coef_shape
        else:
            return output_shape

    def get_config(self):
        config = super().get_config()

        config.update(
            head_size=self.head_size,
            num_heads=self.num_heads,
            output_size=self.output_size,
            dropout=self._droput_rate,
            use_projection_bias=self.use_projection_bias,
            return_attn_coef=self.return_attn_coef,
        )

        return config


class RelPositionMultiHeadAttention(MultiHeadAttention):
    def __init__(self, kernel_sizes=None, strides=None, **kwargs):
        super(RelPositionMultiHeadAttention, self).__init__(**kwargs)

    def build(self, input_shape):
        num_pos_features = input_shape[-1][-1]
        input_max = (self.num_heads * self.head_size) ** -0.5
        self.pos_kernel = self.add_weight(
            name="pos_kernel",
            shape=[self.num_heads, num_pos_features, self.head_size],
            initializer=tf.keras.initializers.RandomUniform(minval=-input_max, maxval=input_max),
        )
        self.pos_bias_u = self.add_weight(
            name="pos_bias_u",
            shape=[self.num_heads, self.head_size],
            initializer=tf.keras.initializers.Zeros(),
        )
        self.pos_bias_v = self.add_weight(
            name="pos_bias_v",
            shape=[self.num_heads, self.head_size],
            initializer=tf.keras.initializers.Zeros(),
        )
        super(RelPositionMultiHeadAttention, self).build(input_shape[:-1])

    @staticmethod
    def relative_shift(x):
        x_shape = tf.shape(x)
        x = tf.pad(x, [[0, 0], [0, 0], [0, 0], [1, 0]])
        x = tf.reshape(x, [x_shape[0], x_shape[1], x_shape[3] + 1, x_shape[2]])
        x = tf.reshape(x[:, :, 1:, :], x_shape)
        return x

    def call(self, inputs, training=False, mask=None, **kwargs):
        query, key, value, pos = inputs

        query, key, value = self.call_qkv(query, key, value, training=training)

        pos = tf.einsum("...MI,HIO->...MHO", pos, self.pos_kernel)

        query_with_u = query + self.pos_bias_u
        query_with_v = query + self.pos_bias_v

        logits_with_u = tf.einsum("...NHO,...MHO->...HNM", query_with_u, key)
        logits_with_v = tf.einsum("...NHO,...MHO->...HNM", query_with_v, pos)
        logits_with_v = self.relative_shift(logits_with_v)

        logits = logits_with_u + logits_with_v[:, :, :, :tf.shape(logits_with_u)[3]]

        depth = tf.constant(self.head_size, dtype=tf.float32)
        logits /= tf.sqrt(depth)

        output, attn_coef = self.call_attention(query, key, value, logits,
                                                training=training, mask=mask)

        if self.return_attn_coef:
            return output, attn_coef
        else:
            return output
