#12. Write a program to find out the mean, median, and mode of 1, 2, 3, 2, 3, 4, 4, 4, 5, 4, 5, 6.

from statistics import mean, median, mode
numbers = [1, 2, 3, 2, 3, 4, 7, 4, 5, 4, 5, 6, 7]

print(f"Mean of the dataset is: {mean(numbers):.2f}")
print(f"Median of the dataset is: {median(numbers)}")
print(f"Mode of the dataset is: {mode(numbers)}")

'''
Output
Mean of the dataset is: 4.08
Median of the dataset is: 4
Mode of the dataset is: 4
'''