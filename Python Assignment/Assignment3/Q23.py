#23. Write a function that returns the index of each vowel in a string using a for loop.

def vowel_indices(input_string):
    indices = []
    
    for index, char in enumerate(input_string):
        if char in "aeiouAEIOU":
            indices.append(index)
    
    return indices

input_str = input("Enter a string: ")
print(f"Indices of vowels in '{input_str}' : {vowel_indices(input_str)}.")

'''
Output
Enter a string: Animesh
Indices of vowels in 'Animesh' : [0, 2, 4].
'''