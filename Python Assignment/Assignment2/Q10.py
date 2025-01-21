'''10. Write a program that takes a string as input and prints out all possible sub-strings of the string using
loops, e.g., if the input is ”abc”, the output should be ”a”, ”ab”, ”abc”, ”b”, ”bc”, ”c”. '''

string = input("Enter a string: ")
length = len(string)

for i in range(length):
    for j in range(i + 1, length + 1):
        print(string[i:j], end = ' ')

'''
Output
Enter a string: Animesh
A An Ani Anim Anime Animes Animesh n ni nim nime nimes nimesh i im ime imes imesh m me mes mesh e es esh s sh h 
'''