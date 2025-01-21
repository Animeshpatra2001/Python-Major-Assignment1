import numpy as np
from scipy import stats  # For mode calculation
# 15. Median and Mode functions
def median(arr):
    return np.median(arr)

def mode(arr):
    return stats.mode(arr, axis=None).mode[0]