#28. Write a function that takes a string of lowercase alphabets as inputs and gives an output by shifting them by one letter ahead. Note that if the string has ’z’, then it will be treated as ’a’. Example: python → qzuipo, pythonzabc → qzuipobbcd.

def shift_string(str_):
    result = ""
    for ch in str_:
        if ch == 'z':
            result += 'a'
        elif ch == 'Z':
            result += 'A'
        else:
            result += chr(ord(ch) + 1)
    return result

str_ = input("Enter string: ")
print(f"'{str_}' after shifting one letter ahead: '{shift_string(str_)}'.")

'''
Output
Enter string: Animesh
'Animesh' after shifting one letter ahead: 'Bojnfti'.
'''
