import numpy as np
from scipy import stats  # For mode calculation
# 7. Most frequent value
array_7 = np.array([695175101, 550890707, 651195387, 963459727, 22])
most_frequent = stats.mode(array_7)