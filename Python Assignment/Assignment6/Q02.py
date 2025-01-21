import numpy as np
from scipy import stats  # For mode calculation
# 2. Use arange to create a 2x2 array and perform operations
array = np.arange(4).reshape(2, 2)
cubed_array = array**3
added_seven = array + 7
multiplied_by_two = array * 2