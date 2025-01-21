#b) 1 + x/1! + x^2/2! + x^3/3! + . . . + x^n/n!

from math import factorial

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))
sum = 0
for i in range(n + 1):
    term = (x ** i) / factorial(i)
    sum += term
print(f"The sum of the series for n = {n} and x = {x} is: {sum}")