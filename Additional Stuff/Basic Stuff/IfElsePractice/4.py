# The date June 10, 1960, is special because when it is written in the following format, the
# month times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and a two digit 
# year. The program should then determine whether the month times the day equals the year. If so, 
# it should display a message saying the date is magic.
# Otherwise, it should display a message saying the date is not magic.

month = int(input("Enter a month in numeric form, ie June is 06: "))
day = int(input("Enter the numeric day: "))
year = int(input("Enter the two digit year, ie 1960 is 60: "))

# if month*day == year:
#     print("The date you entered is magic!")
# else:
#     print("The date you entered is not magic")
# One line magick
print("The date you entered is magic!") if month*day == year else print("The date you entered is not magic")
