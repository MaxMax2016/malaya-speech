import numpy as np

MEL_MEAN = np.array(
    [
        -1.5740001,
        -1.4348104,
        -1.5139098,
        -1.6246336,
        -1.6752515,
        -1.7680025,
        -1.7760286,
        -1.7528734,
        -1.8041315,
        -1.8012472,
        -1.8027176,
        -1.9035194,
        -1.9578964,
        -1.9994992,
        -2.0844033,
        -2.1187687,
        -2.1622295,
        -2.2394779,
        -2.2338855,
        -2.2480168,
        -2.305088,
        -2.292752,
        -2.3084722,
        -2.3356872,
        -2.3130097,
        -2.3548095,
        -2.3716748,
        -2.3779838,
        -2.3913856,
        -2.4077997,
        -2.4266715,
        -2.4421942,
        -2.4601338,
        -2.472935,
        -2.4671652,
        -2.4954624,
        -2.4690363,
        -2.4902608,
        -2.4972625,
        -2.5067022,
        -2.5201054,
        -2.5324624,
        -2.5559728,
        -2.581556,
        -2.5896087,
        -2.6268358,
        -2.63209,
        -2.6385717,
        -2.643181,
        -2.6316028,
        -2.6296246,
        -2.6271076,
        -2.6232407,
        -2.633728,
        -2.6465907,
        -2.6617272,
        -2.682576,
        -2.7137046,
        -2.748443,
        -2.7718158,
        -2.7812696,
        -2.7706382,
        -2.7826896,
        -2.8613455,
        -2.890965,
        -2.9139066,
        -2.9305134,
        -2.947076,
        -2.9644268,
        -2.983897,
        -3.0105824,
        -3.0403843,
        -3.0732262,
        -3.1091833,
        -3.1210651,
        -3.1251779,
        -3.121024,
        -3.1200256,
        -3.1209245,
        -3.1165335,
    ]
)

MEL_STD = np.array(
    [
        1.230472,
        1.327531,
        1.3601356,
        1.3375461,
        1.3238465,
        1.3120779,
        1.3098428,
        1.3213241,
        1.331737,
        1.3353229,
        1.328456,
        1.3090632,
        1.2812053,
        1.258766,
        1.2386954,
        1.2156279,
        1.1853899,
        1.1605514,
        1.140438,
        1.1209714,
        1.1116445,
        1.1039788,
        1.0967629,
        1.0930606,
        1.0867565,
        1.0795456,
        1.0792181,
        1.0771185,
        1.0733371,
        1.0648862,
        1.0592022,
        1.0589684,
        1.0529573,
        1.0430313,
        1.0367931,
        1.0392818,
        1.0390384,
        1.0373435,
        1.0425745,
        1.0392631,
        1.0374379,
        1.0273374,
        1.0158786,
        1.0045007,
        0.9938071,
        0.9857478,
        0.9776848,
        0.9719092,
        0.9747336,
        0.9855356,
        0.9954023,
        1.0040481,
        1.0114045,
        1.0118195,
        1.0090452,
        1.0043728,
        1.0009744,
        0.9930537,
        0.98306245,
        0.97594565,
        0.97142047,
        0.9710727,
        0.9617401,
        0.93079495,
        0.9274678,
        0.9236653,
        0.9165311,
        0.9163408,
        0.9170644,
        0.9204914,
        0.9186133,
        0.91328037,
        0.898893,
        0.874806,
        0.8498537,
        0.8413321,
        0.8457093,
        0.8523416,
        0.8559832,
        0.8640359,
    ]
)

ECAPA_TDNN_WINDOWS = np.array(
    [
        0.08000001311302185,
        0.08005675673484802,
        0.08022701740264893,
        0.08051067590713501,
        0.08090773224830627,
        0.08141803741455078,
        0.08204150199890137,
        0.0827779769897461,
        0.08362725377082825,
        0.08458912372589111,
        0.08566337823867798,
        0.08684971928596497,
        0.08814787864685059,
        0.08955749869346619,
        0.09107831120491028,
        0.09270986914634705,
        0.09445175528526306,
        0.09630361199378967,
        0.0982649028301239,
        0.10033521056175232,
        0.10251399874687195,
        0.1048007607460022,
        0.10719487071037292,
        0.10969573259353638,
        0.11230283975601196,
        0.11501544713973999,
        0.11783286929130554,
        0.12075451016426086,
        0.12377956509590149,
        0.1269073486328125,
        0.13013699650764465,
        0.13346782326698303,
        0.1368989646434784,
        0.1404295265674591,
        0.14405867457389832,
        0.14778554439544678,
        0.15160918235778809,
        0.15552863478660583,
        0.15954294800758362,
        0.16365116834640503,
        0.16785219311714172,
        0.1721450686454773,
        0.1765287220478058,
        0.18100205063819885,
        0.18556392192840576,
        0.19021326303482056,
        0.1949489414691925,
        0.1997697353363037,
        0.20467448234558105,
        0.20966193079948425,
        0.2147308886051178,
        0.2198801338672638,
        0.22510835528373718,
        0.2304142713546753,
        0.23579657077789307,
        0.24125391244888306,
        0.2467850148677826,
        0.2523884177207947,
        0.25806280970573425,
        0.26380670070648193,
        0.26961880922317505,
        0.2754976153373718,
        0.28144165873527527,
        0.28744953870773315,
        0.2935197353363037,
        0.29965072870254517,
        0.30584096908569336,
        0.31208905577659607,
        0.318393349647522,
        0.3247523307800293,
        0.3311644196510315,
        0.337628036737442,
        0.3441416025161743,
        0.35070347785949707,
        0.35731202363967896,
        0.36396563053131104,
        0.37066274881362915,
        0.37740159034729004,
        0.38418057560920715,
        0.3909980058670044,
        0.39785221219062805,
        0.40474146604537964,
        0.41166412830352783,
        0.41861844062805176,
        0.4256027042865753,
        0.4326151907444,
        0.4396541714668274,
        0.44671788811683655,
        0.4538046419620514,
        0.46091267466545105,
        0.46804019808769226,
        0.4751855134963989,
        0.482346773147583,
        0.4895222783088684,
        0.49671024084091187,
        0.5039088726043701,
        0.5111164450645447,
        0.5183310508728027,
        0.5255510807037354,
        0.5327746868133545,
        0.5400000214576721,
        0.5472254157066345,
        0.5544490218162537,
        0.5616689920425415,
        0.5688837170600891,
        0.5760912299156189,
        0.5832898616790771,
        0.5904778242111206,
        0.597653329372406,
        0.6048146486282349,
        0.6119599342346191,
        0.6190874576568604,
        0.62619549036026,
        0.6332822442054749,
        0.6403459906578064,
        0.6473849415779114,
        0.6543974280357361,
        0.661381721496582,
        0.6683359146118164,
        0.6752586364746094,
        0.6821478605270386,
        0.6890020370483398,
        0.6958194971084595,
        0.7025984525680542,
        0.7093373537063599,
        0.7160344123840332,
        0.7226880788803101,
        0.7292966842651367,
        0.7358585596084595,
        0.7423720955848694,
        0.7488356828689575,
        0.7552477717399597,
        0.761606752872467,
        0.7679110765457153,
        0.7741591334342957,
        0.7803494334220886,
        0.7864804267883301,
        0.7925505638122559,
        0.7985584735870361,
        0.8045024871826172,
        0.810381293296814,
        0.8161934018135071,
        0.8219373226165771,
        0.8276116847991943,
        0.8332151174545288,
        0.838746190071106,
        0.8442035913467407,
        0.8495858907699585,
        0.8548917770385742,
        0.8601199984550476,
        0.8652691841125488,
        0.8703380823135376,
        0.8753255605697632,
        0.8802303075790405,
        0.8850511312484741,
        0.8897868394851685,
        0.8944361209869385,
        0.8989980220794678,
        0.9034713506698608,
        0.9078550338745117,
        0.9121478796005249,
        0.916348934173584,
        0.920457124710083,
        0.9244714379310608,
        0.9283908605575562,
        0.9322144985198975,
        0.9359413981437683,
        0.9395705461502075,
        0.9431011080741882,
        0.9465322494506836,
        0.949863076210022,
        0.9530927538871765,
        0.9562205076217651,
        0.9592455625534058,
        0.9621672034263611,
        0.964984655380249,
        0.967697262763977,
        0.9703043103218079,
        0.9728052020072937,
        0.9751993417739868,
        0.9774860739707947,
        0.9796648621559143,
        0.9817351698875427,
        0.983696460723877,
        0.9855483174324036,
        0.9872902035713196,
        0.9889217615127563,
        0.9904425144195557,
        0.9918521642684937,
        0.9931503534317017,
        0.9943366646766663,
        0.9954109191894531,
        0.9963728189468384,
        0.9972220659255981,
        0.9979585409164429,
        0.9985820055007935,
        0.9990923404693604,
        0.9994893670082092,
        0.9997730255126953,
        0.9999432563781738,
        1.0,
        0.9999432563781738,
        0.9997730255126953,
        0.9994893670082092,
        0.9990923404693604,
        0.9985820055007935,
        0.9979585409164429,
        0.9972220659255981,
        0.9963728189468384,
        0.9954109191894531,
        0.9943366050720215,
        0.9931502938270569,
        0.9918521642684937,
        0.9904425144195557,
        0.9889217615127563,
        0.9872901439666748,
        0.9855482578277588,
        0.9836964011192322,
        0.981735110282898,
        0.9796648025512695,
        0.9774860143661499,
        0.9751992225646973,
        0.9728051424026489,
        0.9703042507171631,
        0.9676971435546875,
        0.9649845361709595,
        0.9621671438217163,
        0.959245502948761,
        0.9562203884124756,
        0.9530926942825317,
        0.9498629570007324,
        0.946532130241394,
        0.9431010484695435,
        0.939570426940918,
        0.9359412789344788,
        0.9322144985198975,
        0.9283908605575562,
        0.924471378326416,
        0.920457124710083,
        0.9163488745689392,
        0.9121478199958801,
        0.9078549146652222,
        0.9034712910652161,
        0.898997962474823,
        0.8944361209869385,
        0.8897867202758789,
        0.8850510716438293,
        0.8802303075790405,
        0.8753255605697632,
        0.8703380823135376,
        0.8652690649032593,
        0.8601198196411133,
        0.8548916578292847,
        0.8495857119560242,
        0.8442034721374512,
        0.8387460708618164,
        0.8332149982452393,
        0.8276115655899048,
        0.8219372034072876,
        0.8161932229995728,
        0.8103811740875244,
        0.8045023679733276,
        0.7985582947731018,
        0.7925504446029663,
        0.7864802479743958,
        0.7803492546081543,
        0.7741589546203613,
        0.767910897731781,
        0.7616065740585327,
        0.7552475929260254,
        0.748835563659668,
        0.7423719167709351,
        0.7358583807945251,
        0.7292965054512024,
        0.7226879000663757,
        0.7160342931747437,
        0.7093371748924255,
        0.7025983333587646,
        0.6958193182945251,
        0.6890019178390503,
        0.6821476817131042,
        0.6752583980560303,
        0.6683357954025269,
        0.6613814830780029,
        0.654397189617157,
        0.6473847031593323,
        0.6403457522392273,
        0.6332820057868958,
        0.6261952519416809,
        0.6190872192382812,
        0.61195969581604,
        0.6048144102096558,
        0.5976530909538269,
        0.5904775857925415,
        0.583289623260498,
        0.5760909914970398,
        0.5688834190368652,
        0.5616687536239624,
        0.5544487237930298,
        0.5472253561019897,
        0.5400000214576721,
        0.5327746272087097,
        0.5255510807037354,
        0.5183310508728027,
        0.5111163854598999,
        0.5039088129997253,
        0.4967101812362671,
        0.48952221870422363,
        0.48234671354293823,
        0.47518542408943176,
        0.4680401384830475,
        0.4609125852584839,
        0.4538045823574066,
        0.4467178285121918,
        0.43965408205986023,
        0.43261510133743286,
        0.42560261487960815,
        0.418618381023407,
        0.41166406869888306,
        0.40474140644073486,
        0.3978521227836609,
        0.3909979462623596,
        0.3841805160045624,
        0.37740153074264526,
        0.3706626296043396,
        0.36396557092666626,
        0.3573119044303894,
        0.3507033586502075,
        0.34414148330688477,
        0.33762791752815247,
        0.33116430044174194,
        0.32475221157073975,
        0.3183932304382324,
        0.3120889365673065,
        0.3058408796787262,
        0.2996505796909332,
        0.29351961612701416,
        0.2874494194984436,
        0.2814415693283081,
        0.2754974961280823,
        0.2696186900138855,
        0.26380661129951477,
        0.2580626606941223,
        0.2523882985115051,
        0.24678486585617065,
        0.2412538230419159,
        0.23579645156860352,
        0.23041415214538574,
        0.22510823607444763,
        0.21988001465797424,
        0.21473079919815063,
        0.2096618115901947,
        0.20467433333396912,
        0.19976958632469177,
        0.19494882225990295,
        0.1902131736278534,
        0.1855638027191162,
        0.1810019314289093,
        0.17652860283851624,
        0.17214497923851013,
        0.16785207390785217,
        0.16365104913711548,
        0.15954285860061646,
        0.15552854537963867,
        0.15160906314849854,
        0.14778542518615723,
        0.14405855536460876,
        0.14042943716049194,
        0.13689884543418884,
        0.13346773386001587,
        0.13013693690299988,
        0.12690722942352295,
        0.12377947568893433,
        0.1207544207572937,
        0.11783277988433838,
        0.11501532793045044,
        0.1123027503490448,
        0.1096956729888916,
        0.10719478130340576,
        0.10480067133903503,
        0.10251393914222717,
        0.10033515095710754,
        0.09826484322547913,
        0.09630352258682251,
        0.09445169568061829,
        0.09270983934402466,
        0.09107828140258789,
        0.08955749869346619,
        0.0881478488445282,
        0.08684971928596497,
        0.08566337823867798,
        0.08458912372589111,
        0.08362725377082825,
        0.0827779769897461,
        0.08204150199890137,
        0.08141803741455078,
        0.08090773224830627,
        0.08051067590713501,
        0.08022701740264893,
        0.08005675673484802,
    ]
)
