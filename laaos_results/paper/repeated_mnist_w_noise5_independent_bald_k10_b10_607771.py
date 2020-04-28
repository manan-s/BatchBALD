store = {}
store['args']={'dataset': 'DatasetEnum.repeated_mnist_w_noise5', 'num_inference_samples': 10, 'available_sample_k': 10, 'seed': 607771, 'type': 'AcquisitionFunction.bald', 'acquisition_method': 'AcquisitionMethod.independent', 'experiment_description': 'RMNIST with noise k10 b5 and b10 (and k100 b10), BALD, BatchBALD and heuristic', 'initial_samples': [38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329], 'batch_size': 64, 'scoring_batch_size': 512, 'test_batch_size': 512, 'validation_set_size': 3072, 'early_stopping_patience': 3, 'epochs': 40, 'epoch_samples': 5056, 'target_accuracy': 1.0, 'target_num_acquired_samples': 300, 'initial_percentage': 100, 'reduce_percentage': 0, 'min_remaining_percentage': 100, 'min_candidates_per_acquired_item': 100, 'log_interval': 20, 'experiment_task_id': 'repeated_mnist_w_noise5_independent_bald_k10_b10_607771', 'experiments_laaos': 'experiment_configs/rmnist_w_noise_2_5/configs.py', 'no_cuda': False, 'quickquick': False, 'initial_samples_per_class': 2, 'balanced_validation_set': False, 'balanced_test_set': False}
store['cmdline']=['./src/ignite_mnist.py', '--experiment_task_id=repeated_mnist_w_noise5_independent_bald_k10_b10_607771', '--experiments_laaos=experiment_configs/rmnist_w_noise_2_5/configs.py']
store['iterations']=[]
store['initial_samples']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.6379, 'nll': 1.5570397798080533}, 'chosen_targets': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'chosen_samples': [33233, 213233, 153233, 148294, 273233, 223806, 283806, 88294, 103806, 268294], 'chosen_samples_score': [1.3310584531577008, 1.327569178817214, 1.3259381489176743, 1.3234981370204986, 1.3218368266658078, 1.3212778151254383, 1.3177518785573863, 1.3164998106300774, 1.3164895114628643, 1.314945014892156], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.870544968027389, 'batch_acquisition_elapsed_time': 40.778002362989355})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.6642, 'nll': 1.289636120321917}, 'chosen_targets': [8, 8, 8, 2, 2, 8, 8, 2, 2, 7], 'chosen_samples': [233854, 293854, 173854, 33203, 213203, 113854, 53854, 153203, 93203, 207103], 'chosen_samples_score': [1.462582292385615, 1.4574867528440019, 1.4568136096482707, 1.4557306338818257, 1.4529539076324955, 1.452934880195965, 1.4450531650483318, 1.4414049703269496, 1.4385758317024115, 1.4326679920202978], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 4.951513962005265, 'batch_acquisition_elapsed_time': 40.16135859800852})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.677, 'nll': 1.4880622512392148}, 'chosen_targets': [8, 8, 8, 8, 8, 8, 8, 5, 5, 2], 'chosen_samples': [108739, 228739, 288739, 48739, 168739, 30322, 90322, 242933, 92831, 99726], 'chosen_samples_score': [1.2299618853427199, 1.21303029351775, 1.212551282855678, 1.20952398054259, 1.2012345330685572, 1.1937035754783465, 1.1932362787091189, 1.1923192982050437, 1.1921957398823873, 1.1921893826554513], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.010465658997418, 'batch_acquisition_elapsed_time': 40.67030666698702})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.7319, 'nll': 1.2321933997421495}, 'chosen_targets': [9, 9, 9, 9, 9, 5, 5, 5, 5, 9], 'chosen_samples': [195562, 15562, 135562, 75562, 255562, 280518, 21338, 201338, 100518, 141040], 'chosen_samples_score': [1.7520026487448792, 1.7235543552814594, 1.723133286025892, 1.7182546611073577, 1.6730901374869305, 1.6176868965901092, 1.6169673851596205, 1.6149307357839482, 1.6100051070007673, 1.6099555279573852], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.010975917015458, 'batch_acquisition_elapsed_time': 40.128817129996605})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.7602, 'nll': 0.8877332586225284}, 'chosen_targets': [0, 0, 0, 0, 0, 8, 3, 3, 0, 0], 'chosen_samples': [139899, 79899, 199899, 259899, 19899, 140089, 286666, 183402, 142634, 82144], 'chosen_samples_score': [1.3524684145008892, 1.346833866636186, 1.3442383069741097, 1.3396606084754525, 1.3371353430710542, 1.2991402203244082, 1.2927082753028125, 1.2865391057212632, 1.2849182205969363, 1.2801855570930172], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.045374389010249, 'batch_acquisition_elapsed_time': 39.795891365007265})
store['iterations'].append({'num_epochs': 17, 'test_metrics': {'accuracy': 0.8017, 'nll': 0.7764745774614705}, 'chosen_targets': [8, 8, 8, 8, 8, 8, 8, 8, 8, 8], 'chosen_samples': [257545, 17545, 153979, 159971, 273979, 33979, 279971, 137545, 219971, 213979], 'chosen_samples_score': [1.4360483771820802, 1.415389103232053, 1.4142382969926581, 1.409280054622519, 1.4011203886078878, 1.3989884929932388, 1.3964622038637626, 1.3952369641249973, 1.388338442195896, 1.376295361091594], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 18.143503083992982, 'batch_acquisition_elapsed_time': 40.44799722501193})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.7878, 'nll': 0.7368233036174833}, 'chosen_targets': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'chosen_samples': [27898, 147898, 207898, 87898, 112550, 267898, 191298, 292550, 131298, 71298], 'chosen_samples_score': [1.1306554165159421, 1.1304537743142355, 1.1297309524131138, 1.1287703104505848, 1.1278629393410622, 1.1218884543150516, 1.1213150288382565, 1.1182268629824936, 1.1160726478012821, 1.1148597567390301], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 6.014604127994971, 'batch_acquisition_elapsed_time': 39.93495687600807})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.8031, 'nll': 0.7954011580899956}, 'chosen_targets': [6, 6, 6, 6, 6, 2, 2, 2, 2, 2], 'chosen_samples': [211736, 31736, 91736, 151736, 271736, 75853, 195853, 135853, 15853, 137269], 'chosen_samples_score': [1.4753567405249977, 1.4699370673185113, 1.4687194816950737, 1.4682167452819814, 1.4532696345501783, 1.4152421489247833, 1.404623143466874, 1.4044114285899407, 1.4024660854875366, 1.385835264713477], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.042636174999643, 'batch_acquisition_elapsed_time': 39.845367161004106})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.7901, 'nll': 0.8621446752707983}, 'chosen_targets': [1, 1, 1, 1, 1, 3, 3, 3, 3, 3], 'chosen_samples': [257540, 77540, 197540, 137540, 17540, 103043, 93911, 273911, 33911, 153911], 'chosen_samples_score': [1.3643490517206764, 1.3562834873103953, 1.3511861169634336, 1.351008458443926, 1.3339334854808318, 1.2565396768149868, 1.2557968269871007, 1.242255646166471, 1.2318182831503142, 1.2252339658478464], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.11413267502212, 'batch_acquisition_elapsed_time': 40.20394937400124})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.8011, 'nll': 0.8142732651789847}, 'chosen_targets': [9, 4, 4, 9, 4, 9, 9, 4, 9, 4], 'chosen_samples': [49371, 150875, 270875, 109371, 210875, 229371, 289371, 30875, 169371, 90875], 'chosen_samples_score': [1.3086070017031262, 1.2944597512385618, 1.2932521609322651, 1.2891903176464168, 1.2890456801068195, 1.287098523615976, 1.2870980369558576, 1.2804974291857405, 1.2775390570923406, 1.276462115596372], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.04833944197162, 'batch_acquisition_elapsed_time': 40.23061295799562})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8135, 'nll': 0.651512668768074}, 'chosen_targets': [7, 7, 7, 7, 7, 7, 7, 7, 7, 7], 'chosen_samples': [180651, 240651, 120651, 60651, 651, 120567, 567, 83352, 60567, 240567], 'chosen_samples_score': [1.2118941364812235, 1.2109473600926506, 1.2067435968448454, 1.1933013979150418, 1.1920430037790708, 1.1701296698075292, 1.1414099542917224, 1.1405162248842207, 1.1388064735936816, 1.1376351112047356], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.051556998019805, 'batch_acquisition_elapsed_time': 40.890470004000235})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8293, 'nll': 0.6080004637641852}, 'chosen_targets': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'chosen_samples': [291425, 231425, 111425, 51425, 210315, 171425, 127595, 7595, 90315, 42387], 'chosen_samples_score': [1.3392179919957425, 1.3323881026587945, 1.3300705720365544, 1.3288327227128673, 1.3161170580410027, 1.3145035692375262, 1.308081392256882, 1.2997954271595842, 1.2997270627844129, 1.2994937737802124], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.016840837983182, 'batch_acquisition_elapsed_time': 40.77028487800271})
store['iterations'].append({'num_epochs': 17, 'test_metrics': {'accuracy': 0.8561, 'nll': 0.5774493962660007}, 'chosen_targets': [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 'chosen_samples': [166814, 115064, 46814, 235064, 286814, 106814, 175064, 295064, 55064, 226814], 'chosen_samples_score': [1.3640498794116478, 1.3636027053573296, 1.3554587576573511, 1.3530450407798063, 1.3423785431852941, 1.338669971432615, 1.337308286859611, 1.3320358216496957, 1.3304477266540429, 1.3046109068569005], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 18.044498064991785, 'batch_acquisition_elapsed_time': 40.02319282700773})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8398, 'nll': 0.5608786817748038}, 'chosen_targets': [7, 7, 7, 7, 7, 7, 7, 7, 7, 7], 'chosen_samples': [211684, 31684, 151684, 271684, 91684, 183494, 243494, 63494, 123494, 278098], 'chosen_samples_score': [1.3622327788550552, 1.350951005753516, 1.3456108208623276, 1.342643855010842, 1.327285531487406, 1.3124022119632195, 1.3107047957573856, 1.3080305460603137, 1.302158072258462, 1.298429763491267], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.03669957999955, 'batch_acquisition_elapsed_time': 39.696955767984036})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.8428, 'nll': 0.5412111696319748}, 'chosen_targets': [3, 3, 2, 3, 3, 3, 2, 2, 2, 3], 'chosen_samples': [79495, 139495, 226163, 19495, 259495, 199495, 166163, 46163, 106163, 135472], 'chosen_samples_score': [1.4371643450707952, 1.43374943741239, 1.428272987707399, 1.4254458848083371, 1.422276346285622, 1.4157177212621206, 1.4138592139356705, 1.4116660209663838, 1.4072885606446575, 1.385187445490002], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.154388057999313, 'batch_acquisition_elapsed_time': 40.35068954800954})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.8523, 'nll': 0.4991103174801331}, 'chosen_targets': [4, 4, 4, 4, 4, 7, 7, 7, 7, 7], 'chosen_samples': [8458, 248458, 68458, 188458, 128458, 19949, 259949, 199949, 194833, 254833], 'chosen_samples_score': [1.4919150347558694, 1.4841662330771799, 1.4758911553113623, 1.4699492893041373, 1.4678266109440383, 1.4438791513280287, 1.438890619599668, 1.4341790902301588, 1.4328904200080448, 1.4313373608531634], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.034650220011827, 'batch_acquisition_elapsed_time': 40.06479995400878})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8554, 'nll': 0.4775902639529455}, 'chosen_targets': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'chosen_samples': [45282, 121109, 1109, 225282, 165282, 105282, 285282, 61109, 181109, 241109], 'chosen_samples_score': [1.2962385133581136, 1.286093836769636, 1.2841319330404815, 1.2832360132682659, 1.2828327106924866, 1.2827413302860904, 1.2766504089405881, 1.2752034759978343, 1.2709925023573416, 1.2692290810755165], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.09352962099365, 'batch_acquisition_elapsed_time': 39.80068289299379})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.8457, 'nll': 0.5198062627293769}, 'chosen_targets': [0, 0, 0, 0, 9, 0, 9, 9, 9, 3], 'chosen_samples': [88102, 28102, 148102, 268102, 36438, 208102, 96438, 156438, 276438, 37373], 'chosen_samples_score': [1.4572855319980444, 1.4457709776620895, 1.4454748619442073, 1.4450219862688853, 1.4369983046477266, 1.435737484997615, 1.427489289401458, 1.4122632561717645, 1.4106591814413498, 1.4022983687223851], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.083281856001122, 'batch_acquisition_elapsed_time': 39.89204585700645})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.8449, 'nll': 0.52190393443816}, 'chosen_targets': [9, 9, 9, 9, 3, 9, 7, 9, 7, 7], 'chosen_samples': [53324, 86703, 293324, 233324, 226242, 173324, 39877, 266703, 159877, 219877], 'chosen_samples_score': [1.265436959222477, 1.2588248758630018, 1.2495741619699534, 1.2479954168224314, 1.2394947455137755, 1.2373073487883808, 1.235181351326232, 1.230956981866219, 1.2262472993321234, 1.2251738728977204], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.07454188799602, 'batch_acquisition_elapsed_time': 39.81378537102137})
store['iterations'].append({'num_epochs': 13, 'test_metrics': {'accuracy': 0.8505, 'nll': 0.5244399110721429}, 'chosen_targets': [0, 0, 0, 0, 5, 0, 0, 5, 0, 5], 'chosen_samples': [237686, 117686, 177686, 57686, 19942, 82529, 297686, 139942, 22529, 259942], 'chosen_samples_score': [1.4443491737071463, 1.4129885598125291, 1.4044418958447424, 1.4024458401538138, 1.3861703729085908, 1.3786882200255686, 1.3784609265098229, 1.3771181424560297, 1.3741314665232718, 1.3741256194968223], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.105301660019904, 'batch_acquisition_elapsed_time': 40.33187670301413})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.8638, 'nll': 0.44739001764814956}, 'chosen_targets': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 'chosen_samples': [56551, 268128, 296551, 176551, 116551, 148128, 236551, 88128, 28128, 208128], 'chosen_samples_score': [1.3600737533041718, 1.3502313726921609, 1.3484176649304767, 1.3483151594951048, 1.3471332887631369, 1.340627901961346, 1.335049868192095, 1.3336240617401716, 1.3264295966086443, 1.3171596253890594], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.042431822017534, 'batch_acquisition_elapsed_time': 40.117031269997824})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.8804, 'nll': 0.4237852170431635}, 'chosen_targets': [6, 6, 6, 6, 6, 2, 2, 2, 2, 6], 'chosen_samples': [279036, 99036, 219036, 159036, 39036, 68443, 248443, 8443, 128443, 185517], 'chosen_samples_score': [1.3615058316914757, 1.3586257210565842, 1.3491513574775942, 1.3440296506024179, 1.32923153897912, 1.3221632133663528, 1.317378348284566, 1.3172558013874383, 1.3161761453548932, 1.3117544022516845], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.001542910002172, 'batch_acquisition_elapsed_time': 40.44097673599026})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.8649, 'nll': 0.4549889336002999}, 'chosen_targets': [0, 0, 0, 0, 0, 0, 0, 2, 2, 2], 'chosen_samples': [212693, 32693, 272693, 92693, 279620, 219620, 152693, 249715, 129715, 189715], 'chosen_samples_score': [1.358717977363407, 1.3571958455428297, 1.352196810079064, 1.3456221160618362, 1.3452936528040953, 1.3296820085100018, 1.3278392602277975, 1.3261961722681734, 1.3237986834730713, 1.312016804784997], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.08324050999363, 'batch_acquisition_elapsed_time': 40.976426139997784})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.8874, 'nll': 0.3973331457915228}, 'chosen_targets': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'chosen_samples': [287828, 195462, 15462, 47828, 167828, 135462, 227828, 255462, 75462, 107828], 'chosen_samples_score': [1.191683812035042, 1.1911257789177416, 1.1842435015874524, 1.1809019001150154, 1.1795279664236518, 1.178917725387987, 1.1778666926293047, 1.1775563363026713, 1.172632296646458, 1.1693949509665855], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.14400535900495, 'batch_acquisition_elapsed_time': 40.97607590901316})
store['iterations'].append({'num_epochs': 15, 'test_metrics': {'accuracy': 0.8716, 'nll': 0.45611257859059506}, 'chosen_targets': [9, 3, 9, 3, 3, 3, 3, 9, 9, 9], 'chosen_samples': [60929, 14655, 240929, 254655, 134655, 74655, 194655, 180929, 120929, 929], 'chosen_samples_score': [1.5738185330614383, 1.5675241006088596, 1.5572086716784086, 1.5488139564342998, 1.5469684700298718, 1.5449441343108994, 1.54393426446862, 1.5425760157678807, 1.5365987228129059, 1.5227633262360831], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.152028169017285, 'batch_acquisition_elapsed_time': 40.19679431599798})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.8786, 'nll': 0.42721580152171035}, 'chosen_targets': [8, 8, 9, 9, 8, 9, 9, 9, 7, 9], 'chosen_samples': [64873, 184873, 132768, 72768, 4873, 192768, 252768, 12768, 93131, 27344], 'chosen_samples_score': [1.250829374726961, 1.2360940386002606, 1.2261939605288608, 1.2249704600884597, 1.21452187141045, 1.2132277067866706, 1.21196841446866, 1.2080059846121518, 1.2061036637848785, 1.1952266302915056], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.176877318008337, 'batch_acquisition_elapsed_time': 41.17717082297895})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8924, 'nll': 0.37642683198160537}, 'chosen_targets': [3, 5, 7, 5, 5, 3, 5, 5, 7, 3], 'chosen_samples': [77777, 284736, 150359, 164736, 224736, 137777, 44736, 104736, 270359, 257777], 'chosen_samples_score': [1.096595070784493, 1.090237709391888, 1.087072278790684, 1.086260436121702, 1.0830536984191916, 1.0799909946951445, 1.0798631767599212, 1.0792040435592591, 1.077451196006997, 1.0731411196045508], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.18896152198431, 'batch_acquisition_elapsed_time': 40.9274750900222})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.8951, 'nll': 0.3674039968600113}, 'chosen_targets': [8, 8, 8, 8, 8, 3, 3, 6, 3, 6], 'chosen_samples': [8680, 188680, 68680, 128680, 248680, 46329, 106329, 165274, 226329, 143790], 'chosen_samples_score': [1.2075937291676648, 1.2001037945722872, 1.1982523519718158, 1.1926898639077104, 1.1913484697190757, 1.181094238736065, 1.180836092065164, 1.1771505611997632, 1.1729002686972094, 1.1684079091487973], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.13759746501455, 'batch_acquisition_elapsed_time': 40.54686758000753})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.8911, 'nll': 0.3738150363679755}, 'chosen_targets': [2, 2, 2, 2, 2, 7, 8, 9, 9, 7], 'chosen_samples': [27458, 147458, 267458, 207458, 87458, 247033, 217720, 55834, 295834, 67033], 'chosen_samples_score': [1.2820503866839155, 1.2642597001793896, 1.2435969966514828, 1.21908843137911, 1.2056560083903796, 1.126915312366443, 1.1251850371418868, 1.1244110279995485, 1.1209461819285829, 1.1207392487174985], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.128875730006257, 'batch_acquisition_elapsed_time': 40.59170865098713})
store['iterations'].append({'num_epochs': 13, 'test_metrics': {'accuracy': 0.9004, 'nll': 0.33878691088427415}, 'chosen_targets': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'chosen_samples': [212080, 113598, 152080, 92080, 32080, 53598, 233598, 173598, 293598, 1356], 'chosen_samples_score': [1.2776459066896322, 1.2655388854115042, 1.2600454589292556, 1.2583305011972044, 1.2489239872472855, 1.2446945218405414, 1.2423167445513332, 1.2405992284225125, 1.239257368840333, 1.232618132977502], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.199850327015156, 'batch_acquisition_elapsed_time': 40.02441544699832})