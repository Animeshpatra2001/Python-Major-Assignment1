'''12. Write a Python program using functions that prompt the user to enter today’s date (in the format YYYY-MM-DD) and the current day of the week. Then, ask the user to input a number of days. The program should calculate and display the new date and the day of the week after the specified number of days have passed.
Input:
Today’s date: 2024-08-27
Today’s day: Tuesday
Number of days: 5
Output:
New date: 2024-09-01
New day: Sunday'''

from datetime import datetime, timedelta

def get_input():
    today_date = input("Enter today's date (YYYY-MM-DD): ")
    today_day = input("Enter today's day of the week: ")
    number_of_days = int(input("Enter the number of days to add: "))
    return today_date, today_day, number_of_days

def calculate_new_date(today_date, number_of_days):
    date_format = "%Y-%m-%d"
    date_object = datetime.strptime(today_date, date_format)
    new_date = date_object + timedelta(days = number_of_days)
    return new_date

def calculate_new_day(today_day, number_of_days):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    current_index = days_of_week.index(today_day)
    new_index = (current_index + number_of_days) % 7
    return days_of_week[new_index]

def main():
    today_date, today_day, number_of_days = get_input()
    new_date = calculate_new_date(today_date, number_of_days)
    new_day = calculate_new_day(today_day, number_of_days)
    
    print(f"New date: {new_date.strftime('%Y-%m-%d')}")
    print(f"New day: {new_day}")

if __name__ == "__main__":
    main()
    
'''
Output
Enter today's date (YYYY-MM-DD): 2024-11-06
Enter today's day of the week: Wednesday
Enter the number of days to add: 3
New date: 2024-11-09
New day: Saturday
'''
