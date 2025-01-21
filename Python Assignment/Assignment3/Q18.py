#18. Write a function to check if a string is an Anagram of another string. (An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once, e.g. tom marvolo riddle ⇝ i am lord voldemort)

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    char_count = {}
    
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    for count in char_count.values():
        if count != 0:
            return False
        
    return True

str1, str2 = input("Enter first string: "), input("Enter second string: ")
print(f"'{str1}' and '{str2}' anagrams : {are_anagrams(str1, str2)}")

'''
Output
Enter first string: animesh
Enter second string: hsemina
'animesh' and 'hsemina' anagrams : True
'''