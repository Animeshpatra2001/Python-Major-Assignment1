'''11. Write a program that functions as a simple calculator. It should continuously accept a pair of numbers
and an operator (+, -, *, /) from the user and print the result. If the user types ”exit,” the program
quits. Otherwise the program continues asking for a pair of input numbers. '''

while True:
    operator = input("Enter the operator(+ , - , * , /) or 'exit' to stop: ")
    if operator == 'exit':
        exit()
    if operator in '+-*/':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        match operator:
            case '+':
                print(f"{num1} + {num2} = {num1 + num2}")
            case '-':
                print(f"{num1} - {num2} = {num1 - num2}")
            case '*':
                print(f"{num1} * {num2} = {num1 * num2}")
            case '/':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error! Division by zero is not allowed.")
    else:
        print("Invalid operator. Try again.")

'''
Output
Enter the operator(+ , - , * , /) or 'exit' to stop: *
Enter first number: 20
Enter second number: 30
20 * 30 = 600
'''