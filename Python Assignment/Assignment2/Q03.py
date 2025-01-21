'''3. Write a Python program to calculate a student's letter grade based on their numeric score using the following scale:
A (90-100), B (80-89), C (70-79), D (60-69), and F (below 60). Additionally, provide
a comment for each grade: ”Excellent” for A, ”Good” for B, ”Average” for C, ”Needs Improvement”
for D, and ”Failing” for F.'''

score = float(input("Enter your numeric score: "))

if score >= 90 :
    print("Grade: 'A' \nExcellent!")
elif 80 <= score < 90 :
    print("Grade: 'B' \nGood!")
elif 70 <= score < 80 :
    print("Grade: 'C' \nAverage!")
elif 60 <= score < 70 :
    print("Grade: D \nNeeds Improvement!")
else :
    print("Grade: 'F' \nFailing!")

'''
Output
Enter your numeric score: 91.33
Grade: 'A' 
Excellent!
'''