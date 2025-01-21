import numpy as np
from scipy import stats  # For mode calculation
# 11. Stacking
array1 = np.array([[10, 11], [12, 13]])
array2 = np.array([[4, 5], [6, 7]])
array3 = np.vstack((array1, array2))
array4 = np.hstack((array2, array1))
arr_vstack = np.vstack((array4, array4))
arr_hstack = np.hstack((array3, array3))