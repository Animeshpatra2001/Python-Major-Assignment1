#22. Create a function that prints the first 10 terms of an arithmetic progression.

def print_arithmetic_progression(first_term, common_difference):
    print("First 10 terms of the arithmetic progression: ", end = ' ')
    for n in range(10):
        term = first_term + n * common_difference
        print(term, end=' ')

first_term, common_difference = int(input("Enter first term of AP: ")), int(input("Enter the common difference of AP: "))
print_arithmetic_progression(first_term, common_difference)

'''
Output
Enter first term of AP: 1
Enter the common difference of AP: 3
First 10 terms of the arithmetic progression:  1 4 7 10 13 16 19 22 25 28
'''