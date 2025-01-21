'''
20. Create a program that reads two integers, a and b, from the user. Your program should compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of ab
Hint: You will probably find the log10 function in the math module helpful for computing the
second last item in the list
'''

import math

a =  int(input("Enter first number: "))
b =  int(input("Enter second number: "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(math.log10(a))
print(a * b)

'''
Output
Enter first number: 93
Enter second number: 96
189
-3
8928
0.96875
93
1.968482948553935
8928
'''