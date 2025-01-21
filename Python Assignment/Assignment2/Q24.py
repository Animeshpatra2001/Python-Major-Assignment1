'''24. Write a program that reads an integer from the user and checks which digits (0-9) have appeared in
the number. The program should print out the digits that have appeared, e.g. input=1234, output=
ONE TWO THREE FOUR'''

number = int(input("Enter a number: "))
digits = []
while number > 0 :
    digit = number % 10
    digits.insert(0, digit)
    number //= 10

for i in range(len(digits)) :
    if digits[i] == 0 :
        print("ZERO", end = " ")
    elif digits[i] == 1 :
        print("ONE", end = " ")
    elif digits[i] == 2 :
        print("TWO", end = " ")
    elif digits[i] == 3 :
        print("THREE", end = " ")
    elif digits[i] == 4 :
        print("FOUR", end = " ")
    elif digits[i] == 5 :
        print("FIVE", end = " ")
    elif digits[i] == 6 :
        print("SIX", end = " ")
    elif digits[i] == 7 :
        print("SEVEN", end = " ")
    elif digits[i] == 8 :
        print("EIGHT", end = " ")
    else :
        print("NINE", end = " ")

'''
Output
Enter a number: 963
NINE SIX THREE
'''