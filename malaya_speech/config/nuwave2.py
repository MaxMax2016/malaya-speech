config = {'train': {'batch_size': 12,
                    'lr': '2e-4',
                    'weight_decay': 0.0,
                    'num_workers': 8,
                    'gpus': 2,
                    'opt_eps': '1e-9',
                    'beta1': 0.9,
                    'beta2': 0.99},
          'data': {'timestamp_path': 'vctk-silence-labels/vctk-silences.0.92.txt',
                   'base_dir': '/DATA1/VCTK-0.92/wav48_silence_trimmed/',
                   'dir': '/DATA1/VCTK-0.92/wav48_silence_trimmed_wav/',
                   'format': '*mic1.wav',
                   'cv_ratio': '(100./108., 8./108., 0.00)'},
          'audio': {'filter_length': 1024,
                    'hop_length': 256,
                    'win_length': 1024,
                    'sampling_rate': 48000,
                    'sr_min': 6000,
                    'sr_max': 48000,
                    'length': 32768},
          'arch': {'residual_layers': 15,
                   'residual_channels': 64,
                   'pos_emb_dim': 512,
                   'bsft_channels': 64},
          'logsnr': {'logsnr_min': -20.0, 'logsnr_max': 20.0},
          'dpm': {'max_step': 1000,
                  'pos_emb_scale': 50000,
                  'pos_emb_channels': 128,
                  'infer_step': 8,
                  'infer_schedule': 'tf.constant([-2.6, -0.8, 2.0, 6.4, 9.8, 12.9, 14.4, 17.2])'},
          'log': {'name': 'nuwave2',
                  'checkpoint_dir': 'checkpoint',
                  'tensorboard_dir': 'tensorboard',
                  'test_result_dir': 'test_sample/result'}}

config_torch = {'train': {'batch_size': 12,
                          'lr': '2e-4',
                          'weight_decay': 0.0,
                          'num_workers': 8,
                          'gpus': 2,
                          'opt_eps': '1e-9',
                          'beta1': 0.9,
                          'beta2': 0.99},
                'data': {'timestamp_path': 'vctk-silence-labels/vctk-silences.0.92.txt',
                         'base_dir': '/DATA1/VCTK-0.92/wav48_silence_trimmed/',
                         'dir': '/DATA1/VCTK-0.92/wav48_silence_trimmed_wav/',
                         'format': '*mic1.wav',
                         'cv_ratio': '(100./108., 8./108., 0.00)'},
                'audio': {'filter_length': 1024,
                          'hop_length': 256,
                          'win_length': 1024,
                          'sampling_rate': 48000,
                          'sr_min': 6000,
                          'sr_max': 48000,
                          'length': 32768},
                'arch': {'residual_layers': 15,
                         'residual_channels': 64,
                         'pos_emb_dim': 512,
                         'bsft_channels': 64},
                'logsnr': {'logsnr_min': -20.0, 'logsnr_max': 20.0},
                'dpm': {'max_step': 1000,
                        'pos_emb_scale': 50000,
                        'pos_emb_channels': 128,
                        'infer_step': 8,
                        'infer_schedule': 'torch.tensor([-2.6, -0.8, 2.0, 6.4, 9.8, 12.9, 14.4, 17.2])'},
                'log': {'name': 'nuwave2',
                        'checkpoint_dir': 'checkpoint',
                        'tensorboard_dir': 'tensorboard',
                        'test_result_dir': 'test_sample/result'}}
