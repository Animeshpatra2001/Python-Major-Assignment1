'''20. Write a python program that reads an integer and displays all its smallest factors in increasing order,
e.g., if the input integer is 120, the output should be as follows: 2, 2, 2, 3, 5.'''

number = int(input("Enter a number: "))
factor = 2
factors = []

while number > 1 :
    while number % factor == 0 :
        factors.append(factor)
        number //= factor
    factor += 1

print(f"Factors: {', '.join(map(str, factors))}")

'''
Output
Enter a number: 369
Factors: 3, 3, 41
'''

