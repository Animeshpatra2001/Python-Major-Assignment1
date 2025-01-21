import numpy as np
from scipy import stats  # For mode calculation
# 12. Reimplement stacking with concatenate
array3_concat = np.concatenate((array1, array2), axis=0)
array4_concat = np.concatenate((array2, array1), axis=1)