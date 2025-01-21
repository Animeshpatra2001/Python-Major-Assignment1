'''9. Write a program to find the remainder when a user input number is divided by 5 using match case. If
the user inputs a non-integer, Python should say ”Invalid input” and stop.'''

number = input("Enter a number: ")
isInteger = True
for ch in number:
    if ord(ch) < 48 or ord(ch) > 57 :
        isInteger = False

if isInteger:
    print(f"The remainder dividing number with 5 is: {int(number) % 5}")
else :
    print("Invalid input")

'''
Output
Enter a number: 99
The remainder dividing number with 5 is: 4
'''