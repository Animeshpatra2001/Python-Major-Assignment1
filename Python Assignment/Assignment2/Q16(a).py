#a) 1 - x^2/2! + x^4/4! - x^6/6! + . . . + x^2n/(2n)!

from math import factorial

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))
sum = 0
for i in range(n + 1):
    term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    sum += term

print(f"The sum of the series for n={n} and x={x} is: {sum}")

