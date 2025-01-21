#25. Write a function to check if two numbers are coprime.

def are_coprime(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1 == 1

num1, num2 = int(input("Enter first number: ")), int(input("Enter second number: "))
print(f"{num1} and {num2} are coprime : {are_coprime(num1, num2)}")

'''
Output
Enter first number: 7
Enter second number: 11
7 and 11 are coprime : True
'''