#18. Write a Python program that prints all numbers from 1 to 100, except multiples of 7, using a for loop with continue.

for i in range(1, 100) :
    if i % 7 == 0 :
        continue
    print(i, end = ' ')