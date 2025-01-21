'''22. Write a program that takes a number from the user and continuously sums its digits until the sum
becomes a single-digit number.'''

number = int(input("Enter a number: "))
sum = 0

while number > 0 :
    sum += number % 10
    number = number // 10
    if number == 0 and sum > 9:
        number = sum
        sum = 0
print(f"The single digit sum is: {sum}")

'''
Output
Enter a number: 963
The single digit sum is: 9
'''