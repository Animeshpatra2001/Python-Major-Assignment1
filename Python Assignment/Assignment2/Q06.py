#6. Write a program that takes an integer input from the user and prints whether it is prime or not.

from math import sqrt

num = int(input("Enter a number: "))
if num == 1 or num == 0 :
    print(f"{num} is a special number")
    exit()
    
count = 0
for i in range (2 , int(sqrt(num))):
    if num % i == 0 :
        count += 1

if count > 0 :
    print(f"{num} is not a prime number.")
else :
    print(f"{num} is a prime number.")

'''
Output
Enter a number: 99
99 is not a prime number.
'''