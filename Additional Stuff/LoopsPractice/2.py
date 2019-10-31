# 2. Calories Burned
# Running on a particular treadmill you burn 3.9 calories per minute. 
# Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30minutes.

def main():

    min_cal = 3.9

    for i in range(10, 31, 5):
        cal = i * min_cal
        print(f"You burned {cal:.2f} calories " f"in {i:} minutes")

main()