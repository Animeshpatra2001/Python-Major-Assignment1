#6. Define a function to check if a given string is a palindrome. Example: madam ⟲ madam, racecar ⟲ racecar.

def is_palindrome(string):
    i, j = 0, len(string) - 1
    while i <= j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

string = input("Enter a string: ")
print(f"{string} a palindrome : {is_palindrome(string)}")

'''
Output
Enter a string: racecar
racecar a palindrome : True
'''
