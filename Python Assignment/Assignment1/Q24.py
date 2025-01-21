'''24. Write a program that reads three integers from the user and displays them in sorted order (from
smallest to largest). Use the min and max functions to find the smallest and largest values. The middle
value can be found by computing the sum of all three values, and then subtracting the minimum value
and the maximum value.'''

a , b , c = int(input("Enter first number: ")) , int(input("Enter second number: ")) , int(input("Enter third number: ")) 

max_num = max(a, b, c)
min_num = min(a, b, c)
mid_num = (a + b + c) - (max_num + min_num)

print(f"{min_num} < {mid_num} < {max_num}")

'''
Output
Enter first number: 9
Enter second number: 6
Enter third number: 3
3 < 6 < 9
'''