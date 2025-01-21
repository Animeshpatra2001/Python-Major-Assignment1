#21. Write a function to calculate the factorial of a number using a loop.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}.")

'''
Output
Enter a number: 3
The factorial of 3 is 6.
'''