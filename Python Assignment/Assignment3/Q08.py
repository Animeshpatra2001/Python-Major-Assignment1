'''8. Write a Python program that takes the name of a month as input and returns the number of days in that month.
Input: The name of the Month: February
Output: No. of days: 28/29 days'''

def number_of_days(month):
    days_in_month = {
        "January": "31",
        "February": "28/29",
        "March": "31",
        "April": "30",
        "May": "31",
        "June": "30",
        "July": "31",
        "August": "31",
        "September": "30",
        "October": "31",
        "November": "30",
        "December": "31"
    }
    return days_in_month[month]

month = input("Enter name of the month: ")
print(f"There are {number_of_days(month)} days in the month of {month}.")

'''
Output
Enter name of the month: August
There are 31 days in the month of August.
'''
