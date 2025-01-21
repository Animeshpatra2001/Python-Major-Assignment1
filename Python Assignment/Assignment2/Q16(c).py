#c) 1-3+5-7+9-. . .

n = int(input("Enter the number of terms (n): "))
sum = 0
for i in range(n):
    term = (2 * i + 1)
    if i % 2 == 0:
        sum += term
    else:
        sum -= term
print(f"The sum of the series for n={n} terms is: {sum}")