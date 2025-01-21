#14. Write a function to determine if a given number is an Armstrong number. (An Armstrong number is a number that is equal to the sum of its digits, each raised to the power of the number of digits, e.g., 153 = 1^3 + 5^3 + 3^3 , 1634 = 1^4 + 6^4 + 3^4 + 4^4 ).

def is_armstrong_number(num):
    num_str = str(num)
    power = len(num_str)

    armstrong_sum = sum(int(digit) ** power for digit in num_str)
    return armstrong_sum == num

number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

'''
Output
Enter a number: 153
153 is an Armstrong number.
'''