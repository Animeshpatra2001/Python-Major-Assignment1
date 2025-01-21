'''17. Write a python program that displays all the numbers from 100 to 1,000, ten per line, that are divisible
by 5 or 6. Numbers are separated by exactly one space.'''

count = 0
for i in range(100, 1000) :
    if count == 10 :
        print()
        count = 0
    if i % 5 == 0 or i % 6 == 0 :
        print(i, end = ' ')
        count += 1

