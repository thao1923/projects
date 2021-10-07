def clean_output(output, raw_score_factor):
    indexes = np.array([i for (i,j) in enumerate(output["detection_scores"]) if j>=raw_score_factor])
    print(output.keys())
    for key in output.keys():
        if key != "num_detections":
            output[key] = output[key][indexes]
    return output

import numpy as np
output = {'raw_detection_boxes': np.array([[ 4.03258950e-03, -1.75348297e-03,  8.08897987e-02,
         8.16109627e-02],
       [-2.87972130e-02, -7.48390406e-02,  1.13723218e-01,
         1.65302992e-01],
       [-3.95068526e-02, -4.35338803e-02,  1.65767938e-01,
         1.23885378e-01],
       [ 1.62537023e-03,  3.73489484e-02,  7.39790201e-02,
         1.38769627e-01],
       [-2.55326070e-02, -6.24603629e-02,  1.18040979e-01,
         2.37332106e-01],
       [-5.22709563e-02, -2.20460147e-02,  1.50444806e-01,
         1.92418411e-01],
       [ 5.69595210e-03,  7.22545534e-02,  5.69491163e-02,
         1.70704037e-01],
       [-1.48369037e-02, -6.62121326e-02,  1.07911170e-01,
         2.81567991e-01],
       [-6.18476532e-02, -4.84220684e-03,  1.41674414e-01,
         2.24279240e-01],
       [ 5.07946685e-03,  1.39173970e-01,  4.11075428e-02,
         2.29119107e-01],
       [-1.36395469e-02, -1.92175359e-02,  1.04752459e-01,
         3.82883012e-01],
       [-7.28654042e-02,  5.28340042e-02,  1.44834667e-01,
         2.91121364e-01],
       [ 4.15629614e-03,  1.88868403e-01,  3.19795422e-02,
         2.80743212e-01],
       [-8.08304176e-03,  1.65430158e-02,  1.02040142e-01,
         4.50462520e-01],
       [-7.48329610e-02,  1.07522935e-01,  1.45654514e-01,
         3.35951924e-01],
       [ 2.86622811e-03,  2.45507762e-01,  2.91903168e-02,
         3.33396137e-01],
       [-8.26592743e-03,  7.07949996e-02,  1.01652920e-01,
         5.07474661e-01],
       [-8.00914913e-02,  1.64761573e-01,  1.48926213e-01,
         3.87967557e-01],
       [ 2.32932623e-03,  3.00982803e-01,  2.77874358e-02,
         3.85504931e-01],
       [-8.31507891e-03,  1.28028095e-01,  1.00312799e-01,
         5.59185147e-01],
       [-8.09822679e-02,  2.19319999e-01,  1.48168311e-01,
         4.40837383e-01],
       [ 2.28459202e-03,  3.55774641e-01,  2.81263292e-02,
         4.39655244e-01],
       [-9.19409096e-03,  1.87908128e-01,  9.92509872e-02,
         6.10470951e-01],
       [-8.11419189e-02,  2.76307374e-01,  1.46332681e-01,
         4.94590729e-01],
       [ 2.78037880e-03,  4.08485502e-01,  2.88680643e-02,
         4.93023843e-01],
       [-9.56064463e-03,  2.39719227e-01,  9.95066464e-02,
         6.65105700e-01],
       [-8.08141679e-02,  3.28392655e-01,  1.46114185e-01,
         5.48856974e-01],
       [ 2.71769613e-03,  4.60853547e-01,  2.88836583e-02,
         5.45464694e-01],
       [-8.98186117e-03,  2.90678859e-01,  9.98439416e-02,
         7.19178915e-01],
       [-7.96923190e-02,  3.81155282e-01,  1.46064848e-01,
         6.00715220e-01],
       [ 3.00349854e-03,  5.13502598e-01,  3.00349090e-02,
         5.98546028e-01],
       [-9.08949971e-03,  3.45860749e-01,  1.01195842e-01,
         7.71615028e-01],
       [-7.69456252e-02,  4.32410955e-01,  1.47431642e-01,
         6.55570507e-01],
       [ 3.64993047e-03,  5.66519320e-01,  3.13246287e-02,
         6.51074946e-01],
       [-9.13256407e-03,  3.99410903e-01,  1.01671942e-01,
         8.24058712e-01],
       [-7.70590305e-02,  4.85415429e-01,  1.48237869e-01,
         7.08347678e-01],
       [ 4.18212637e-03,  6.18679106e-01,  3.20604891e-02,
         7.02244461e-01],
       [-8.31836089e-03,  4.48993206e-01,  1.01507947e-01,
         8.76144648e-01],
       [-7.75192901e-02,  5.36670148e-01,  1.47279710e-01,
         7.59516776e-01],
       [ 5.05820755e-03,  6.71768844e-01,  3.43094058e-02,
         7.56132424e-01],
       [-8.00509751e-03,  5.07009208e-01,  1.03408754e-01,
         9.26160872e-01],
       [-7.28714019e-02,  5.91394246e-01,  1.48567885e-01,
         8.13289583e-01],
       [ 5.79097122e-03,  7.24545062e-01,  3.47567871e-02,
         8.08067858e-01],
       [-7.71927834e-03,  5.56800485e-01,  1.02770008e-01,
         9.80922103e-01],
       [-7.52296895e-02,  6.43060625e-01,  1.48878098e-01,
         8.65547121e-01],
       [ 5.09337801e-03,  7.77894258e-01,  3.42498384e-02,
         8.62554431e-01],
       [-1.00214407e-02,  6.12569809e-01,  1.02486767e-01,
         1.03641570e+00],
       [-7.53110275e-02,  6.95276916e-01,  1.49028808e-01,
         9.22580063e-01],
       [ 5.79514634e-03,  8.21055353e-01,  3.45806032e-02,
         9.25017059e-01],
       [-8.56509805e-03,  6.64328694e-01,  1.04609080e-01,
         1.09085512e+00],
       [-6.18396103e-02,  7.44969964e-01,  1.48671731e-01,
         9.83424783e-01],
       [ 3.40730697e-03,  8.60921085e-01,  3.18225995e-02,
         9.69811618e-01],
       [-6.90562651e-03,  7.08972514e-01,  1.01154119e-01,
         1.11019468e+00],
       [-6.26665652e-02,  7.98860013e-01,  1.44362107e-01,
         1.00885367e+00],
       [ 8.06442276e-03,  9.36151505e-01,  4.12941873e-02,
         1.00405288e+00],
       [-6.77487999e-03,  8.06603551e-01,  1.05347946e-01,
         1.12845743e+00],
       [-6.86139017e-02,  8.82087827e-01,  1.82094440e-01,
         1.03339362e+00],
       [ 1.58506930e-02, -1.68226659e-04,  1.25622749e-01,
         7.84875378e-02],
       [ 3.07612866e-03, -5.56039400e-02,  1.43120229e-01,
         1.73427641e-01],
       [-2.95844451e-02, -1.55382156e-02,  1.87684268e-01,
         1.18128136e-01],
       [ 2.61765532e-02,  3.04747969e-02,  1.23676747e-01,
         1.42216146e-01],
       [ 3.61115485e-03, -3.07961255e-02,  1.48760080e-01,
         2.22105816e-01],
       [-1.92912370e-02,  3.40796262e-03,  1.81949899e-01,
         1.81896836e-01],
       [ 3.06691527e-02,  6.77009448e-02,  1.21355370e-01,
         1.81682259e-01],
       [ 2.41666287e-03, -4.29685339e-02,  1.57727122e-01,
         2.89703488e-01],
       [-3.70445326e-02,  5.55434078e-03,  1.87853783e-01,
         2.40095556e-01],
       [ 3.45535874e-02,  1.31885707e-01,  1.18244678e-01,
         2.25731254e-01],
       [ 1.00776330e-02, -1.84512436e-02,  1.57199800e-01,
         3.77428919e-01],
       [-5.73032796e-02,  5.34729883e-02,  1.84713662e-01,
         2.94085652e-01],
       [ 3.75520326e-02,  1.90893412e-01,  1.14931583e-01,
         2.75354862e-01],
       [ 1.95821375e-02,  2.97871977e-02,  1.57160908e-01,
         4.38804090e-01],
       [-5.54749072e-02,  1.13149956e-01,  1.79460138e-01,
         3.40522289e-01],
       [ 3.79779674e-02,  2.42517188e-01,  1.16771743e-01,
         3.29060525e-01],
       [ 2.01065615e-02,  8.61910582e-02,  1.59374207e-01,
         4.85698879e-01],
       [-4.27379608e-02,  1.69342920e-01,  1.78318977e-01,
         3.89431715e-01],
       [ 3.70048024e-02,  2.95720994e-01,  1.18377805e-01,
         3.80558729e-01],
       [ 1.78298354e-02,  1.41004935e-01,  1.64670646e-01,
         5.33992589e-01],
       [-3.72858495e-02,  2.21839070e-01,  1.88166320e-01,
         4.41582441e-01],
       [ 4.05358449e-02,  3.48371029e-01,  1.17720939e-01,
         4.35459018e-01],
       [ 2.24317908e-02,  1.93848640e-01,  1.67599067e-01,
         5.89441061e-01],
       [-3.34205404e-02,  2.71345198e-01,  1.92657292e-01,
         5.00086069e-01],
       [ 3.90004888e-02,  4.05909628e-01,  1.21259905e-01,
         4.86509889e-01],
       [ 2.15739533e-02,  2.49364540e-01,  1.67447478e-01,
         6.46612704e-01],
       [-3.78317162e-02,  3.27075809e-01,  1.89820528e-01,
         5.53645372e-01],
       [ 3.65478396e-02,  4.57681090e-01,  1.23575121e-01,
         5.41140020e-01],
       [ 1.86431035e-02,  3.07386607e-01,  1.66688234e-01,
         6.96656704e-01],
       [-3.90853733e-02,  3.80865633e-01,  1.87539458e-01,
         6.08640373e-01],
       [ 3.59251946e-02,  5.08265615e-01,  1.21639475e-01,
         5.95507741e-01],
       [ 1.64309815e-02,  3.60897720e-01,  1.67394131e-01,
         7.47531831e-01],
       [-4.05715778e-02,  4.28633988e-01,  1.90488994e-01,
         6.66174114e-01],
       [ 3.57614942e-02,  5.60255826e-01,  1.21315390e-01,
         6.48500502e-01],
       [ 1.52237937e-02,  4.16582137e-01,  1.67208552e-01,
         7.96494961e-01],
       [-4.13341075e-02,  4.81080890e-01,  1.93126500e-01,
         7.19172001e-01],
       [ 3.53289284e-02,  6.12850845e-01,  1.22486278e-01,
         7.00590909e-01],
       [ 1.48999318e-02,  4.71778810e-01,  1.67141646e-01,
         8.46169889e-01],
       [-4.45721224e-02,  5.34947693e-01,  1.95548147e-01,
         7.70465434e-01],
       [ 3.65461260e-02,  6.65822744e-01,  1.22378632e-01,
         7.54137993e-01],
       [ 1.53131336e-02,  5.28775752e-01,  1.66620746e-01,
         8.95266354e-01],
       [-4.47011814e-02,  5.88379979e-01,  1.97285056e-01,
         8.23974609e-01],
       [ 3.61488461e-02,  7.19152510e-01,  1.22987360e-01,
         8.04763854e-01]], dtype=np.float32), 'detection_scores': np.array([0.6690273 , 0.61671555, 0.6159135 , 0.6159135 , 0.6159135 ,
       0.6159135 , 0.6159135 , 0.6159135 , 0.6159135 , 0.5701807 ,
       0.56624055, 0.547525  , 0.51722115, 0.4935293 , 0.49257433,
       0.4856769 , 0.47992828, 0.46082902, 0.44392475, 0.44062898,
       0.43528366, 0.42405483, 0.41377655, 0.40272814, 0.3934399 ,
       0.38620314, 0.38348514, 0.382412  , 0.37922928, 0.37523222,
       0.37523222, 0.37523222, 0.37523222, 0.3733106 , 0.36989298,
       0.347925  , 0.33130962, 0.3146662 , 0.31187594, 0.31034145,
       0.30346748, 0.2963265 , 0.28942487, 0.28754678, 0.28737816,
       0.28676918, 0.27755532, 0.27654698, 0.276116  , 0.27150327,
       0.2702991 , 0.2647316 , 0.26346153, 0.262069  , 0.25156376,
       0.24530977, 0.24213432, 0.24139524, 0.24077813, 0.23835492,
       0.23795024, 0.22299396, 0.21770854, 0.21757673, 0.2167858 ,
       0.21212406, 0.2115828 , 0.20937812, 0.20548767, 0.20384912,
       0.19157296, 0.19064273, 0.18646105, 0.15982378, 0.14677025,
       0.14497112, 0.14131235, 0.14022088, 0.13531572, 0.13372815,
       0.13306151, 0.1319163 , 0.12844451, 0.12749818, 0.127053  ,
       0.12679328, 0.12600175, 0.12555274, 0.12001298, 0.11971356,
       0.11759946, 0.1168493 , 0.11630927, 0.11498109, 0.11396123,
       0.11333276, 0.11307445, 0.1102267 , 0.1085583 , 0.10696736],
      dtype=np.float32), 'raw_detection_scores': np.array([[0.00648572, 0.27150327],
       [0.0065077 , 0.12749818],
       [0.00645227, 0.04562131],
       [0.0063498 , 0.19157296],
       [0.00638779, 0.08300187],
       [0.00635407, 0.01741254],
       [0.00579242, 0.07244211],
       [0.00589214, 0.03675969],
       [0.0057835 , 0.0028833 ],
       [0.00506823, 0.01536927],
       [0.00514967, 0.00916904],
       [0.00506372, 0.00147647],
       [0.00474832, 0.00523368],
       [0.00482616, 0.00300972],
       [0.00473906, 0.0010823 ],
       [0.00467933, 0.00477399],
       [0.00475453, 0.00237148],
       [0.00467667, 0.00117717],
       [0.00460557, 0.00492162],
       [0.00467641, 0.00227792],
       [0.00460255, 0.00108876],
       [0.00461433, 0.0053331 ],
       [0.00467881, 0.00238225],
       [0.00461408, 0.00117469],
       [0.00460425, 0.0050642 ],
       [0.00466883, 0.00242453],
       [0.00460626, 0.00114224],
       [0.00463524, 0.0050706 ],
       [0.00470116, 0.00231242],
       [0.00463518, 0.00111348],
       [0.00467615, 0.00599442],
       [0.00474282, 0.00277745],
       [0.00467172, 0.00118692],
       [0.00468858, 0.00610569],
       [0.00475718, 0.00287108],
       [0.00468556, 0.00117342],
       [0.00469133, 0.00596681],
       [0.00476333, 0.00273249],
       [0.00468551, 0.00099523],
       [0.00475594, 0.00694989],
       [0.00482588, 0.00330453],
       [0.00475192, 0.0011799 ],
       [0.00473866, 0.00639175],
       [0.00481168, 0.00302568],
       [0.00473303, 0.00100473],
       [0.00471135, 0.00612694],
       [0.00478299, 0.0033739 ],
       [0.00471061, 0.00108956],
       [0.00490477, 0.00745188],
       [0.00497417, 0.00604992],
       [0.00491283, 0.00209975],
       [0.00521904, 0.01097599],
       [0.00528732, 0.00584401],
       [0.00520915, 0.00347105],
       [0.00511223, 0.01700116],
       [0.00516525, 0.0051358 ],
       [0.0050951 , 0.00582031],
       [0.00664569, 0.21757673],
       [0.00672659, 0.10476076],
       [0.00672923, 0.08211476],
       [0.00692001, 0.23835492],
       [0.00703459, 0.27755532],
       [0.00697834, 0.09793916],
       [0.00628002, 0.07835619],
       [0.00647229, 0.19406548],
       [0.00632842, 0.02378812],
       [0.0056823 , 0.02299633],
       [0.00587401, 0.03277264],
       [0.00573881, 0.00314858],
       [0.00556015, 0.01462834],
       [0.00572123, 0.01072936],
       [0.005602  , 0.0012411 ],
       [0.00567967, 0.01519917],
       [0.00582435, 0.01112248],
       [0.00571898, 0.0015268 ],
       [0.00570544, 0.01680754],
       [0.00585914, 0.01373503],
       [0.00575675, 0.00217331],
       [0.0056586 , 0.01839982],
       [0.0058143 , 0.01551582],
       [0.00570878, 0.00220564],
       [0.0055728 , 0.01690726],
       [0.00571516, 0.01133864],
       [0.0056235 , 0.0014749 ],
       [0.00569436, 0.02019855],
       [0.00583972, 0.01486381],
       [0.00574789, 0.00188128],
       [0.00573387, 0.02408879],
       [0.0058915 , 0.02215122],
       [0.00579382, 0.00258977],
       [0.00578702, 0.02859291],
       [0.00595332, 0.02870758],
       [0.00585028, 0.00332029],
       [0.00580496, 0.03204124],
       [0.00597819, 0.03273451],
       [0.00587078, 0.00389964],
       [0.00585171, 0.04012305],
       [0.00602932, 0.03998444],
       [0.00591485, 0.00462282],
       [0.00581628, 0.03660328]], dtype=np.float32), 'detection_anchor_indices': np.array([1.709e+03, 1.691e+03, 1.155e+03, 1.161e+03, 1.167e+03, 1.173e+03,
       1.179e+03, 1.185e+03, 1.191e+03, 1.149e+03, 1.703e+03, 1.697e+03,
       1.197e+03, 1.131e+03, 1.685e+03, 1.251e+03, 1.095e+03, 1.233e+03,
       1.227e+03, 1.125e+03, 1.245e+03, 1.239e+03, 1.221e+03, 1.089e+03,
       1.119e+03, 1.113e+03, 1.137e+03, 1.143e+03, 1.101e+03, 1.158e+03,
       1.170e+03, 1.182e+03, 1.194e+03, 1.107e+03, 1.215e+03, 1.083e+03,
       1.201e+03, 1.692e+03, 1.255e+03, 1.152e+03, 1.135e+03, 1.099e+03,
       6.510e+02, 4.800e+02, 1.209e+03, 1.237e+03, 6.100e+01, 1.704e+03,
       1.698e+03, 0.000e+00, 1.231e+03, 1.254e+03, 1.129e+03, 1.249e+03,
       1.243e+03, 1.200e+03, 1.225e+03, 1.109e+03, 7.410e+02, 6.000e+01,
       1.220e+03, 1.123e+03, 1.117e+03, 5.700e+01, 1.686e+03, 8.790e+02,
       1.257e+03, 1.105e+03, 6.480e+02, 1.219e+03, 3.000e+00, 1.147e+03,
       1.603e+03, 1.214e+03, 1.635e+03, 5.940e+02, 1.569e+03, 1.213e+03,
       1.629e+03, 1.287e+03, 1.190e+02, 1.281e+03, 3.660e+02, 1.000e+00,
       3.390e+02, 4.980e+02, 1.275e+03, 1.575e+03, 7.440e+02, 6.540e+02,
       1.739e+03, 7.080e+02, 1.293e+03, 1.641e+03, 1.880e+02, 1.110e+02,
       4.440e+02, 1.305e+03, 6.810e+02, 9.090e+02], dtype=np.float32), 'detection_multiclass_scores': np.array([[0.00880205, 0.6690273 ],
       [0.00900591, 0.61671555],
       [0.00923834, 0.6159135 ],
       [0.00923834, 0.6159135 ],
       [0.00923834, 0.6159135 ],
       [0.00923834, 0.6159135 ],
       [0.00923834, 0.6159135 ],
       [0.00923834, 0.6159135 ],
       [0.00923834, 0.6159135 ],
       [0.00904052, 0.5701807 ],
       [0.00902292, 0.56624055],
       [0.00900698, 0.547525  ],
       [0.00882265, 0.51722115],
       [0.00872767, 0.4935293 ],
       [0.00874355, 0.49257433],
       [0.00859575, 0.4856769 ],
       [0.00862472, 0.47992828],
       [0.00847983, 0.46082902],
       [0.00840137, 0.44392475],
       [0.0084086 , 0.44062898],
       [0.00836132, 0.43528366],
       [0.00830929, 0.42405483],
       [0.00826163, 0.41377655],
       [0.00836825, 0.40272814],
       [0.00817377, 0.3934399 ],
       [0.00813328, 0.38620314],
       [0.00829149, 0.38348514],
       [0.00828719, 0.382412  ],
       [0.00811691, 0.37922928],
       [0.00921578, 0.37523222],
       [0.00921578, 0.37523222],
       [0.00921578, 0.37523222],
       [0.00921578, 0.37523222],
       [0.00807284, 0.3733106 ],
       [0.00805676, 0.36989298],
       [0.00814745, 0.347925  ],
       [0.0088167 , 0.33130962],
       [0.0091575 , 0.3146662 ],
       [0.00860891, 0.31187594],
       [0.00902317, 0.31034145],
       [0.00871693, 0.30346748],
       [0.00862368, 0.2963265 ],
       [0.00593061, 0.28942487],
       [0.00545901, 0.28754678],
       [0.00765484, 0.28737816],
       [0.00849256, 0.28676918],
       [0.00703459, 0.27755532],
       [0.00916582, 0.27654698],
       [0.00914691, 0.276116  ],
       [0.00648572, 0.27150327],
       [0.00841381, 0.2702991 ],
       [0.00858637, 0.2647316 ],
       [0.00841531, 0.26346153],
       [0.00837362, 0.262069  ],
       [0.00832139, 0.25156376],
       [0.00881093, 0.24530977],
       [0.00827356, 0.24213432],
       [0.00807589, 0.24139524],
       [0.00553142, 0.24077813],
       [0.00692001, 0.23835492],
       [0.0080616 , 0.23795024],
       [0.00818366, 0.22299396],
       [0.00814474, 0.21770854],
       [0.00664569, 0.21757673],
       [0.00886056, 0.2167858 ],
       [0.00524324, 0.21212406],
       [0.00724137, 0.2115828 ],
       [0.00812415, 0.20937812],
       [0.00571704, 0.20548767],
       [0.00806795, 0.20384912],
       [0.0063498 , 0.19157296],
       [0.00825501, 0.19064273],
       [0.00790595, 0.18646105],
       [0.00766136, 0.15982378],
       [0.00681513, 0.14677025],
       [0.00589784, 0.14497112],
       [0.00677409, 0.14131235],
       [0.00766461, 0.14022088],
       [0.00672774, 0.13531572],
       [0.00671523, 0.13372815],
       [0.0064841 , 0.13306151],
       [0.00670083, 0.1319163 ],
       [0.00480922, 0.12844451],
       [0.0065077 , 0.12749818],
       [0.00551624, 0.127053  ],
       [0.00460205, 0.12679328],
       [0.00665286, 0.12600175],
       [0.00664915, 0.12555274],
       [0.00541822, 0.12001298],
       [0.00581239, 0.11971356],
       [0.00868402, 0.11759946],
       [0.00582883, 0.1168493 ],
       [0.00657069, 0.11630927],
       [0.00655905, 0.11498109],
       [0.00593075, 0.11396123],
       [0.00639965, 0.11333276],
       [0.00442884, 0.11307445],
       [0.0065166 , 0.1102267 ],
       [0.00541307, 0.1085583 ],
       [0.00488221, 0.10696736]], dtype=np.float32), 'detection_classes': np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 'detection_boxes': np.array([[0.00000000e+00, 6.57766819e-01, 3.65125567e-01, 9.85863209e-01],
       [0.00000000e+00, 1.07395858e-01, 3.95176530e-01, 4.91785854e-01],
       [0.00000000e+00, 9.17387158e-02, 3.28954130e-01, 4.09198046e-01],
       [0.00000000e+00, 1.91738740e-01, 3.28954130e-01, 5.09198070e-01],
       [0.00000000e+00, 2.91738749e-01, 3.28954130e-01, 6.09198034e-01],
       [0.00000000e+00, 3.91738713e-01, 3.28954130e-01, 7.09198058e-01],
       [0.00000000e+00, 4.91738737e-01, 3.28954130e-01, 8.09198081e-01],
       [0.00000000e+00, 5.91738701e-01, 3.28954130e-01, 9.09198046e-01],
       [0.00000000e+00, 6.91738725e-01, 3.28954130e-01, 1.00000000e+00],
       [0.00000000e+00, 0.00000000e+00, 3.23578477e-01, 3.08004260e-01],
       [0.00000000e+00, 5.29465199e-01, 4.03735459e-01, 9.19618368e-01],
       [0.00000000e+00, 3.17811221e-01, 4.13453341e-01, 6.98755622e-01],
       [7.83234835e-04, 7.88498640e-01, 3.17996770e-01, 1.00000000e+00],
       [0.00000000e+00, 6.87736869e-01, 2.15674952e-01, 1.00000000e+00],
       [0.00000000e+00, 0.00000000e+00, 3.50134015e-01, 2.99008340e-01],
       [8.66646767e-02, 6.97083116e-01, 4.06589150e-01, 1.00000000e+00],
       [0.00000000e+00, 9.19699073e-02, 2.10287333e-01, 4.06426966e-01],
       [8.82933736e-02, 3.98080051e-01, 4.02544379e-01, 7.07010090e-01],
       [8.93791765e-02, 2.98760861e-01, 3.99804771e-01, 6.06779695e-01],
       [0.00000000e+00, 5.96700907e-01, 2.01214805e-01, 9.06376719e-01],
       [8.99282098e-02, 5.99110246e-01, 3.98405701e-01, 9.06661868e-01],
       [9.06362385e-02, 4.99566168e-01, 3.96587193e-01, 8.06508422e-01],
       [9.12794918e-02, 1.99985743e-01, 3.94920647e-01, 5.06367564e-01],
       [0.00000000e+00, 0.00000000e+00, 2.07505941e-01, 3.03746194e-01],
       [0.00000000e+00, 5.00155807e-01, 1.92220137e-01, 8.05974722e-01],
       [0.00000000e+00, 4.01125163e-01, 1.90428704e-01, 7.05986738e-01],
       [0.00000000e+00, 7.84129560e-01, 2.05888599e-01, 1.00000000e+00],
       [3.02343220e-02, 0.00000000e+00, 3.05799305e-01, 2.03210175e-01],
       [0.00000000e+00, 1.99783623e-01, 1.90787315e-01, 5.05613506e-01],
       [2.39847451e-02, 4.15612161e-02, 2.73883343e-01, 4.59485024e-01],
       [2.39847451e-02, 2.41561234e-01, 2.73883343e-01, 6.59485042e-01],
       [2.39847451e-02, 4.41561222e-01, 2.73883343e-01, 8.59485030e-01],
       [2.39847451e-02, 6.41561210e-01, 2.73883343e-01, 1.00000000e+00],
       [0.00000000e+00, 3.01666558e-01, 1.88311502e-01, 6.05806649e-01],
       [9.39859450e-02, 1.01811111e-01, 3.87747854e-01, 4.05758679e-01],
       [0.00000000e+00, 0.00000000e+00, 2.02975512e-01, 2.02273875e-01],
       [0.00000000e+00, 8.31901729e-01, 4.07533169e-01, 1.00000000e+00],
       [0.00000000e+00, 0.00000000e+00, 3.07646453e-01, 5.92473149e-01],
       [1.39479488e-02, 7.34091878e-01, 4.75819230e-01, 9.69378233e-01],
       [3.06046382e-02, 0.00000000e+00, 2.72741497e-01, 3.58047336e-01],
       [0.00000000e+00, 7.33251929e-01, 3.12471867e-01, 9.69061852e-01],
       [0.00000000e+00, 1.34211570e-01, 2.96549857e-01, 3.68531555e-01],
       [5.52770913e-01, 4.21971619e-01, 6.23307288e-01, 4.84679937e-01],
       [4.08465654e-01, 4.43927348e-01, 4.75673109e-01, 4.83543932e-01],
       [9.90081131e-02, 5.50009310e-03, 3.73626381e-01, 3.04548025e-01],
       [1.24964714e-02, 4.35563028e-01, 4.73696738e-01, 6.67809784e-01],
       [3.61115485e-03, 0.00000000e+00, 1.48760080e-01, 2.22105816e-01],
       [0.00000000e+00, 4.21516240e-01, 3.07940364e-01, 1.00000000e+00],
       [0.00000000e+00, 1.98845088e-01, 3.12282503e-01, 8.06216061e-01],
       [4.03258950e-03, 0.00000000e+00, 8.08897987e-02, 8.16109627e-02],
       [1.15026534e-02, 3.36558700e-01, 4.72244173e-01, 5.66747487e-01],
       [1.30066603e-01, 6.44509017e-01, 3.62389237e-01, 1.00000000e+00],
       [0.00000000e+00, 6.36659980e-01, 2.80667424e-01, 8.66342664e-01],
       [1.09917372e-02, 6.37066841e-01, 4.71497655e-01, 8.66205096e-01],
       [1.03241801e-02, 5.37727237e-01, 4.70522493e-01, 7.65500069e-01],
       [3.79189849e-02, 7.39016294e-01, 2.71599174e-01, 1.00000000e+00],
       [9.70898569e-03, 2.38332123e-01, 4.69623983e-01, 4.64854032e-01],
       [0.00000000e+00, 3.31539571e-01, 2.48413771e-01, 5.76138556e-01],
       [6.77559912e-01, 3.11261788e-03, 7.37389982e-01, 3.62008139e-02],
       [2.61765532e-02, 3.04747969e-02, 1.23676747e-01, 1.42216146e-01],
       [2.78722048e-02, 7.88190812e-02, 4.50039566e-01, 4.32176948e-01],
       [0.00000000e+00, 5.39503574e-01, 2.70486087e-01, 7.63511300e-01],
       [0.00000000e+00, 4.39961076e-01, 2.67178982e-01, 6.63112998e-01],
       [1.58506930e-02, 0.00000000e+00, 1.25622749e-01, 7.84875378e-02],
       [0.00000000e+00, 0.00000000e+00, 2.82205880e-01, 3.89103770e-01],
       [7.76158273e-01, 4.49528039e-01, 8.45034182e-01, 4.80310798e-01],
       [1.03751525e-01, 8.09456706e-01, 3.59013498e-01, 1.00000000e+00],
       [0.00000000e+00, 2.40304857e-01, 2.73073614e-01, 4.62522954e-01],
       [5.63587189e-01, 3.94712985e-01, 6.40644908e-01, 4.40641046e-01],
       [7.02275336e-03, 1.40932202e-01, 4.65703368e-01, 3.62074137e-01],
       [1.62537023e-03, 3.73489484e-02, 7.39790201e-02, 1.38769627e-01],
       [3.75897735e-02, 0.00000000e+00, 4.36777055e-01, 1.61340356e-01],
       [4.98031229e-01, 5.36819398e-01, 1.00000000e+00, 7.58109033e-01],
       [2.56817043e-02, 0.00000000e+00, 4.43198621e-01, 3.36805224e-01],
       [8.08154106e-01, 1.13725424e-01, 1.00000000e+00, 4.01946425e-01],
       [5.32439113e-01, 4.28297698e-01, 6.13397121e-01, 4.87582564e-01],
       [7.08550215e-01, 1.41474307e-02, 9.42363858e-01, 3.01816612e-01],
       [1.54499710e-03, 4.60333377e-02, 4.57721055e-01, 2.56606758e-01],
       [8.08991611e-01, 1.46264285e-02, 1.00000000e+00, 3.01669776e-01],
       [2.09109515e-01, 3.14756125e-01, 4.40254658e-01, 6.01630092e-01],
       [0.00000000e+00, 2.03313902e-02, 2.13474542e-01, 1.61196351e-01],
       [2.09244728e-01, 2.14905664e-01, 4.39738214e-01, 5.01584411e-01],
       [3.23113769e-01, 4.48016673e-01, 3.61322254e-01, 4.71679240e-01],
       [0.00000000e+00, 0.00000000e+00, 1.13723218e-01, 1.65302992e-01],
       [2.63394862e-01, 9.68708217e-01, 3.22960705e-01, 9.92453158e-01],
       [4.30289805e-01, 7.68014729e-01, 4.74574208e-01, 7.83237159e-01],
       [2.09690735e-01, 1.15405783e-01, 4.38015997e-01, 4.01431859e-01],
       [7.09724903e-01, 1.15444526e-01, 9.37882900e-01, 4.01420057e-01],
       [6.83669508e-01, 4.44251299e-02, 7.27124035e-01, 9.40821916e-02],
       [5.63805997e-01, 4.60991859e-01, 6.43769443e-01, 5.43205380e-01],
       [0.00000000e+00, 6.92036629e-01, 5.38647771e-01, 1.00000000e+00],
       [6.15832090e-01, 4.15447623e-01, 7.01975226e-01, 4.92076069e-01],
       [2.10438028e-01, 4.16268975e-01, 4.35061693e-01, 7.01169848e-01],
       [8.10542166e-01, 2.16391876e-01, 1.00000000e+00, 5.01132667e-01],
       [1.65810883e-02, 2.06940904e-01, 2.88593024e-01, 3.95288408e-01],
       [3.18548381e-02, 9.23375905e-01, 1.36353180e-01, 9.94124115e-01],
       [3.82471025e-01, 8.19964707e-01, 4.10656512e-01, 8.35286438e-01],
       [2.10918397e-01, 6.16841853e-01, 4.33113366e-01, 9.00996745e-01],
       [5.62706292e-01, 9.52749968e-01, 6.30641162e-01, 9.91797566e-01],
       [7.93966830e-01, 9.74508703e-01, 8.40265810e-01, 9.92313683e-01]],
      dtype=np.float32), 'num_detections': 100}
print(output.keys())
print(output["detection_scores"])
# output_cleaned = clean_output(output,0.5)
# print(output_cleaned["detection_boxes"])

# for i in range(5):
#     print(output["detection_multiclass_scores"][i])
#     print(output["raw_detection_scores"][i])
#     print(output["detection_scores"][i])
#     print(output["detection_classes"][i])
#     print(output["detection_boxes"][i])
#     print("-"*10)
# 
#indexes = np.array([j for (i,j) in enumerate(output["detection_scores"]) if i>=0.5])

# print(min(output["detection_scores"]))
# test = np.array([1,2,3,4,5])
# print(test[[0,1]])