#17. Create a function that takes a string and returns a new string where all the vowels are removed.

def remove_vowels(str_):
    result = ""
    for i in range(len(str_)):
        if str_[i] not in 'aeiouAEIOU':
            result += str_[i]
    return result

print(remove_vowels('I am a good boy'))

'''
Output
m  gd by
'''
