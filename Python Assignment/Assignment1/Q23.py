'''23. Write a program that reads a four-digit integer from the user and displays the sum of its digits. For
example, if the user enters 3141 then your program should display 3 + 1 + 4 + 1 = 9.'''

num = int(input("Enter a number: "))

last_digit = num % 10
digits_in_number = str(last_digit) + " "
sum = last_digit
num //= 10

while (num > 0) :
    digit = num % 10
    digits_in_number = str(digit) + " + " + digits_in_number
    sum += digit
    num //= 10

print(f"{digits_in_number} = {sum}")

'''
Output
Enter a number: 369
3 + 6 + 9  = 18
'''