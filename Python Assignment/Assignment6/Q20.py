import pandas as pd

s = pd.Series([1, 1, 3, 7, 88, 12, 88, 23, 3, 1, 9, 0])

# Find the index of the first occurrence of the smallest and largest value
min_index = s.idxmin()
max_index = s.idxmax()

print(f"Index of smallest value: {min_index}, Index of largest value: {max_index}")
