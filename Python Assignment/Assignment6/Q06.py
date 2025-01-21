import numpy as np
from scipy import stats  # For mode calculation
# 6. Powers of 2
powers_array = np.array([2**i for i in range(6)]).reshape(2, 3)
flattened = powers_array.flatten()
raveled = powers_array.ravel()