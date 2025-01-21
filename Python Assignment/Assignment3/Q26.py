#26. Write a function that replaces all vowels in a string with the character ”*”.

def replace_vowels(str_):
    for ch in str_:
        if ch in 'aeiouAEIOU':
            str_ = str_.replace(ch, '*')
    return str_

str_ = input("Enter string: ")
print(f"'{str_}' after replacing all the vowels with '*' : '{replace_vowels(str_)}'")

'''
Output
Enter string: Animesh
'Animesh' after replacing all the vowels with '*' : '*n*m*sh'
'''