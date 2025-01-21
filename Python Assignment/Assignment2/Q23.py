'''23. Write a program to simulate a simple ATM withdrawal system. The user can enter an amount they
want to withdraw, and the program will provide the number of 100, 50, 20, and 10 denomination notes
required to dispense that amount. The program should check if the requested amount is a multiple of
10 and if the ATM has enough cash.'''

TOTAL_BALANCE = 10000

count_100, count_20, count_50, count_10 = 0, 0, 0, 0

withdrawal_amount = int(input("Enter withdraw amount: "))

if withdrawal_amount > TOTAL_BALANCE:
    print("Insufficient balance.")
elif withdrawal_amount % 10 != 0:
    print("Withdrawal amount should be a multiple of 10.")
else:
    count_100 = withdrawal_amount // 100
    remaining = withdrawal_amount % 100
    
    count_50 = remaining // 50
    remaining = remaining % 50

    count_20 = remaining // 20
    remaining = remaining % 20

    count_10 = remaining // 10

    print(f"100$ notes: {count_100}\n50$ notes: {count_50}\n20$ notes: {count_20}\n10$ notes: {count_10}")

'''
Output
Enter withdraw amount: 930
100$ notes: 9
50$ notes: 0
20$ notes: 1
10$ notes: 1
'''