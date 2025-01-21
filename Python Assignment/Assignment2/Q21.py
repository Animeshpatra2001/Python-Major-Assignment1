#21. Write a python program to determine whether or not a number n is a factorial number.

n = int(input("Enter a number: "))
number = n
i, factorial = 1, 1

while n > factorial:
    factorial *= i
    i += 1

if n == factorial: 
    print(f"{number} is a factorial number of {i - 1}")
else :
    print(f"{number} is not a factorial number")

'''
Output
Enter a number: 24
24 is a factorial number of 4
'''