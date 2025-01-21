'''8. Write a program that takes an integer input from the user. Use a while loop to continuously prompt
for input until the user enters a positive number. If the final number is even, multiply it by 2 and if it
is odd, square it. Display the results at the end. '''

num = int(input("Enter a number: "))
while num < 0:
    num = int(input("Enter a number: "))

print(num * 2) if num % 2 == 0 else print(num ** 2)

'''
Output
Enter a number: 99
9801
'''