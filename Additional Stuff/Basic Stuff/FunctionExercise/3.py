# 3. How Much Insurance?Many financial experts advise that property owners should insure their homes or buildings for at least 
# 80 percent of the amount it would cost to replace the structure. Write aprogram that asks the user to enter the replacement 
# cost of a building and then displays the minimum amount of insurance he or she should buy for the property.
value = 1 
def main():
    global value
    value = float(input("Enter the replacement cost of your building: "))
    insurance = min_insurance()
    print("The minimum insurance you would want is $", insurance)

def min_insurance():
    return value*.8

main()