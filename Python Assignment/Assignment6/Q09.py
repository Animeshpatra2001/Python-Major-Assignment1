import numpy as np
from scipy import stats  # For mode calculation
# 9. Format 2D array
def format_2d_array(arr):
    max_width = max(len(str(item)) for row in arr for item in row)
    return "\n".join(" ".join(f"{item:>{max_width}}" for item in row) for row in arr)