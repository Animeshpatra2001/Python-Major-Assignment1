#16. Write a function to implement a basic calculator that can add, subtract, multiply, and divide two numbers based on user input.

def calculator():
    print("Welcome to the Basic Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Enter choice ( 1 | 2 | 3 | 4 | 5 ): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero is not allowed.")
                    continue
                print(f"{num1} / {num2} = {(num1 / num2):.2f}")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid operation.")

calculator()

'''
Output
Welcome to the Basic Calculator!
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Enter choice ( 1 | 2 | 3 | 4 | 5 ): 3
Enter first number: 3
Enter second number: 9
3.0 * 9.0 = 27.0
'''