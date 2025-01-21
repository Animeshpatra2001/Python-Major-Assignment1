import numpy as np

# Create a 4x4 array with random values
arr = np.random.rand(4, 4)

# Sort each column
sorted_arr = np.sort(arr, axis=0)
print(sorted_arr)
