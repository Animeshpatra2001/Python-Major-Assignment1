'''12. Write a program that begins by reading a radius, r, from the user. The program will continue by
computing and displaying the area of a circle with radius r and the volume of a sphere with radius r.
Use the pi constant in the math module in your calculations.
Hint: The area of a circle is computed using the formula area = πr^2 .
The volume of a sphere is computed using the formula volume = 4/3(πr^3) .'''

import math

r = int(input("Enter the radius: "))
print(f"The area of the circle with radius {r} is: {math.pi * (r**2)}")
print(f"The volume of a sphere with radius {r} is: {(4/3) * math.pi * (r**3)}")