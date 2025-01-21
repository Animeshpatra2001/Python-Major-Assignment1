'''22. Write a program that begins by reading a temperature from the user in degrees Celsius. Then your
program should display the equivalent temperature in degrees Fahrenheit and degrees Kelvin. The
calculations needed to convert between different units of temperature can be found on the Internet. '''

temperature_in_celsius = float(input("Enter the temperature in celcius scale: "))

print("In Fahrenhit:", temperature_in_celsius * 9/5 + 32)
print("In Kelvin:", temperature_in_celsius + 273.15)

'''
Output

Enter the temperature in celcius scale: 273
In Fahrenhit: 523.4
In Kelvin: 546.15
'''