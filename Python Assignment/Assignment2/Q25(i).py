for i in range(5):
    if i == 0 or i == 5 - 1:
        print('* ' * 5)
    else:
        print('*', end='')
        print(' ' * (5 + 2), end='')
        print('*')

'''
Output
* * * * * 
*       *
*       *
*       *
* * * * * 
'''