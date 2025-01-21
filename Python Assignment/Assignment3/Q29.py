#29. Write a function to check if a given number is a perfect number. (A number is called a perfect number if it is equal to the sum of its real divisors, e.g., 6=1+2+3, 28=1+2+4+7+14).

def is_perfect_number(num):
    if num <= 0:
        return False
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i
    return num == sum

num = int(input("Enter a number: "))
print(f"{num} is a perfect number: {is_perfect_number(num)}")


'''
Output
Enter a number: 6
6 is a perfect number: True
'''