# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:51:21 2022

@author: user
"""

import sys
if sys.version_info >= (3,8):
    import pickle
else:
    import pickle5 as pickle
import data_utils
import os
import numpy as np
import data_utils

with open('data/dataset_audio_patterns_midi.pickle', 'rb') as handle:
    patterns = pickle.load(handle)

# %% XY matrices

x = np.zeros( ( len( patterns ) , len( patterns[0]['audio'] ) ) ).astype(np.float32)
y = np.zeros( ( len( patterns ) , patterns[0]['midi'].size ) ).astype(np.bool)

for i, p in enumerate( patterns ):
    if i%1000 == 0:
        print(str(i) + ' / ' + str(len(patterns)))
    x[i,:] = p['audio'].astype(np.float32)
    y[i,:] = p['midi'].astype(np.bool)

# %% 

with open('data/x.pickle', 'wb') as handle:
    pickle.dump(x, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('data/y.pickle', 'wb') as handle:
    pickle.dump(y, handle, protocol=pickle.HIGHEST_PROTOCOL)