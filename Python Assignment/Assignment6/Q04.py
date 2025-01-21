import numpy as np
from scipy import stats  # For mode calculation
# 4. Swap rows and columns
array_to_swap = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
swapped_array = array_to_swap[[1, 0, 2], :][:, [1, 0, 2]]