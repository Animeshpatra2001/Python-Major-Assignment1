'''13. Positions on a chess board are identified by a letter and a number. The letter identifies the column,
while the number identifies the row, as shown below in Figure 1:
Write a program that reads a position from the user and identify the proper color of the respective
box. '''

position = input("Enter a position on chess board: ")
column = position[0]
row = int(position[1])

if 0 < row < 9 and column in 'abcdefgh':
    if (ord(column) + row) % 2 == 0 :
        print(f"{column}{row} is a white box.")
    else :
        print(f"{column}{row} is a black box.")
else:
    print("Enter a valid position.")

'''
Output
Enter a position on chess board: a3
a3 is a white box.
'''