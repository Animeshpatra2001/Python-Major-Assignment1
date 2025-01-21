#24. Write a function that removes all punctuation from a string.

from string import punctuation as pun

def remove_punctuations(str_):
    return ''.join(ch for ch in str_ if ch not in pun)

str_ = input("Enter a string: ")
print(f"'{str_}' after removing all punctuations is '{remove_punctuations(str_)}'.")

'''
Output
Enter a string: "In choosing both, you lose both."
'"In choosing both, you lose both."' after removing all punctuations is 'In choosing both you lose both'.
'''