#7. Write a Python function to check whether an alphabet is a vowel or consonant.

def is_vowel(character):
    if character in 'aeiouAEIOU':
        return True
    return False

character = input("Enter a character: ")
if is_vowel(character):
    print(f"{character} is a vowel.")
else:
    print(f"{character} is a consonant.")
    
'''
Output
Enter a character: A
A is a vowel.
'''
