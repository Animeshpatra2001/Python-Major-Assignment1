import numpy as np
from scipy import stats  # For mode calculation
# 3. Multiply 3x3 arrays
array1 = np.arange(2, 19, 2).reshape(3, 3)
array2 = np.arange(9, 0, -1).reshape(3, 3)
multiplied_arrays = array1 * array2