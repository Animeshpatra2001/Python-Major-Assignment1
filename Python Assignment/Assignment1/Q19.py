'''19. The program that you create for this exercise will begin by reading the cost of a meal ordered at a
restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local
tax rate when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount
(without the tax). The output from your program should include the tax amount, the tip amount, and
the grand total for the meal including both the tax and the tip. Format the output so that all of the
values are displayed using two decimal places.'''

cost = float(input("Enter the cost of a meal: "))

tax = cost * 0.15
tip = cost * 0.18

print(f"Tax amount: {tax:.2f}")
print(f"Tip amount: {tip:.2f}")

print(f"Total amount: {(cost + tax + tip):.2f}")

'''
Output

Enter the cost of a meal: 50
Tax amount: 7.50
Tip amount: 9.00
Total amount: 66.50
'''