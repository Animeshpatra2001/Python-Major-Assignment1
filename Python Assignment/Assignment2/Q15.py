'''15. Write a function to determine whether a given natural number is a perfect number. A natural number
is said to be a perfect number if it is the sum of its divisors. For Example, 6 is a perfect number
because 6 = 1+2+3, but 15 is not a perfect number because 15!= 1+3+5.'''

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if (num % i) == 0:
       sum += i

print(num, "is a perfect number.") if num == sum else print(num, "is not a perfect number.")

'''
Output
Enter a number: 6
6 is a perfect number.
'''