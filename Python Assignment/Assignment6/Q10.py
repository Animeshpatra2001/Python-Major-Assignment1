import numpy as np
from scipy import stats  # For mode calculation
# 10. Reshape and indexing
array_10 = np.arange(1, 16).reshape(3, 5)
row_2 = array_10[2, :]
column_5 = array_10[:, 4]
rows_0_1 = array_10[:2, :]
columns_2_4 = array_10[:, 2:5]
element_row1_col4 = array_10[1, 4]
subset = array_10[1:, [0, 2, 4]]
