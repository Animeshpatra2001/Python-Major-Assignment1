'''2. Write a program such that Python will ask you if it is raining or not. If your answer is ”yes”, Python
will say ”Carry an umbrella”. If you say ”no”, Python will say ”No need to carry an umbrella”. If
you type anything else, Python will say ”Bye”.'''

response = input("Is it raining ? : ")

if response.lower() == 'yes':
    print('Carry an umbrella.')
elif response.lower() == 'no':
    print('No need to carry an umbrella.')
else :
    print('Bye.')

'''
Output
Is it raining ? : no
No need to carry an umbrella.
'''