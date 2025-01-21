import numpy as np
from scipy import stats  # For mode calculation
# 14. bincount function
random_array = np.random.randint(0, 100, (5, 5))
bincounts = np.bincount(random_array.flatten())