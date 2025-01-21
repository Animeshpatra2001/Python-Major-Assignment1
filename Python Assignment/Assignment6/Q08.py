import numpy as np
from scipy import stats  # For mode calculation
# 8. Create array with linspace and convert to int
linspace_array = np.linspace(1.1, 6.6, 3).reshape(2, 3)
converted_array = linspace_array.astype(int)