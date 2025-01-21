'''25. Create a program that reads duration from the user as a number of days, hours, minutes, and seconds.
Compute and display the total number of seconds represented by this duration.'''

days = int(input("Enter number of days: "))
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
seconds = int(input("Enter number of seconds: "))

total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
print(f"Total seconds: {total_seconds}")

'''
Output
Enter number of days: 3
Enter number of hours: 6
Enter number of minutes: 9
Enter number of seconds: 12
Total seconds: 281352
'''