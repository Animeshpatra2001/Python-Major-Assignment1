#4. Write a function that takes a string as input and returns the reversed string.

def reverse_string(string):
    reverse = ""
    for i in range(len(string) - 1, -1, -1):
        reverse += string[i]
    return reverse

string = input("Enter a string: ")
print(f"Reversed string: {reverse_string(string)}")

'''
Output
Enter a string: Animesh
Reversed string: hseminA
'''
