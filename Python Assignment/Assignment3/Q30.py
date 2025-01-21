#30. Write a function that inputs a number and returns the product of digits of that number.

def product_of_digits(num):
    if num == 0:
        return 0
    product = 1
    while num > 0:
        product *= num % 10
        num //= 10
    return product

num = int(input("Enter a number: "))
print(f"Product of digits of {num}: {product_of_digits(num)}")

'''
Output
Enter a number: 369
Product of digits of 369: 162
'''