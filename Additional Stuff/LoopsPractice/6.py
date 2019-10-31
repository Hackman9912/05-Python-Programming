# 6. Celsius to Fahrenheit Table
# Write a program that displays a table of the Celsius temperatures 0 through 20 and theirFahrenheit equivalents. 
# The formula for converting a temperature from Celsius toFahrenheit is
# F = (9/5)C + 32 where F is the Fahrenheit temperature and C is the Celsius temperature. 
# Your programmust use a loop to display the table.

for cel in range(0, 21):
    fahr = (9/5)* cel +32
    print(f"{cel:} celcius is", f"{fahr:.2f} fahrenheit")

