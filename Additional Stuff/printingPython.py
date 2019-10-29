# Write a program that displays the following information:
# • Your name
# • Your address, with city, state, and ZIP
# • Your telephone number
# • Your MOS

# Input data
name = input("Input your name here please ")
addy = input("Put in your address as: address, city, state, ZIP ")
phone = input("Put your phone number in now ")
MOS = input("Please put your MOS or AFSC in now ")

# Output data
print('{:>5}'.format("Your info is as follos: "), 
    name, addy, phone, MOS
    )

# A company has determined that its annual profit is typically 23 
# percent of total sales. Write a program that asks the user to enter 
# the projected amount of total sales, and then displays the profit 
# that will be made from that amount

# Get the sales
projected_sales=float(input("Input your projected amount of total sales: "))

# Calc the profit

profit=projected_sales*.23

# Output the data
print(f"Profit should be{profit}")


#  One acre of land is equivalent to 43,560 square feet. Write a 
# program that asks the user to enter the total square feet in a tract 
# of land and calculates the number of acres in the tract.

# Input the data
feet=float(input("Input the number of square feet in your tract of land "))

# Do the math
acre=feet/43560

print(f"You have {acre} acres in your land")

# A customer in a store is purchasing five items. Write a program that 
# asks for the price of each item, and then displays the subtotal of 
# the sale, the amount of sales tax, and the total. Assume the sales 
# tax is 6 percent.

# Input the data

count = input("Enter the number of items you purchased")

i = 0

While i < count:

    i += 1
    item(count) = float(input("Enter the value of your item, "))

