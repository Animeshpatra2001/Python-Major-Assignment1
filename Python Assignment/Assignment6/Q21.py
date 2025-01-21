import pandas as pd

L = ['Cry', 'Apple', 'Orange', 'Sky', 'Banana']
s = pd.Series(L)

# Series with elements that have a vowel
has_vowel = s[s.str.contains('[aeiouAEIOU]')]

# Series with elements that start with a vowel
starts_with_vowel = s[s.str.match('^[aeiouAEIOU]')]

print("Elements with a vowel:", has_vowel)
print("Elements starting with a vowel:", starts_with_vowel)
