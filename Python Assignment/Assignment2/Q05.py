#5. Write a program that takes a year as input and determines whether it is a leap year or not.

year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is a leap year.")
else : 
    print(f"{year} is not a leap year.")

'''
Output
Enter a year: 2001
2001 is not a leap year.
'''