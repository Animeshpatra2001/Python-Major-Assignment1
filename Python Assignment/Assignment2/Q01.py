'''1. Write a program such that Python will ask you if it is raining or not. If your answer is ”yes”, Python
will say ”Carry an umbrella”. If you type anything else, Python will say ”Bye”.'''

response = input("Is it raining ? : ")

if response.lower() == 'yes':
    print('Carry an umbrella.')
else :
    print('Bye.')

'''
Output
Is it raining ? : yes
Carry an umbrella.
'''