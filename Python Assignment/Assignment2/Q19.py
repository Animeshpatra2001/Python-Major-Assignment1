#19. Write a python program that accepts a positive integer n and reverses the order of its digits, e.g., 1234 becomes 4321.

num = int(input("Enter a number: "))
num2 = num
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10

print(f"Reverse of {num2} is: {reverse}")

'''
Output
Enter a number: 963
Reverse of 963 is: 369
'''