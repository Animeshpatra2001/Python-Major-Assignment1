for i in range(1, 5 + 1):
    print(' ' * (5 - i) * 2, end='')
    for j in range(i, 0, -1):
        print(j, end=' ')
    for j in range(2, i + 1):
        print(j, end=' ')
    print()

'''
Output
        1 
      2 1 2 
    3 2 1 2 3 
  4 3 2 1 2 3 4 
5 4 3 2 1 2 3 4 5 
'''