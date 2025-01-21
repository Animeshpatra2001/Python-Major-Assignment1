import numpy as np
from scipy import stats  # For mode calculation
# 16. Extract a subarray
array_16 = np.random.random((9, 9, 2))
subarray = array_16[:5, :5, :]