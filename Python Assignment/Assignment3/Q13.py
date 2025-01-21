#13. Write a program that converts a Roman numeral to its integer equivalent.

def roman_to_integer(roman):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman):
        current_value = roman_values[char]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value

    return total

roman_numeral = input("Enter a Roman numeral: ").strip().upper()
integer_value = roman_to_integer(roman_numeral)
print(f"The integer equivalent of '{roman_numeral}' is: {integer_value}")

'''
Output
Enter a Roman numeral: iii
The integer equivalent of 'III' is: 3
'''