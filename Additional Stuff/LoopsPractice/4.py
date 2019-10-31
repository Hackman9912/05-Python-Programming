# 4. Distance Traveled
# The distance a vehicle travels can be calculated as follows:distance = speed* time
# For example, if a train travels 40 miles per hour for three hours, the distance traveled is 120miles. 
# Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled. 
# It should then use a loop to display the distance thevehicle has traveled for each hour of that time period.
def main():
    speed = int(input("Enter the speed of the vehicle in MPH: "))
    hours = int(input("Enter the number of hours the vehicle traveled that speed: "))

    for i in range(hours+1):
        distance = i * speed
        print(f"Your vehicle traveled {distance:} miles in", i, "hours.")

main()