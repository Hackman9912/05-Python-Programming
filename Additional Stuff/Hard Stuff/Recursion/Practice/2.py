"""
2. Recursive Multiplication
    Design a recursive function that accepts two arguments into the parameters x and y. The
    function should return the value of x times y. Remember, multiplication can be performed
    as repeated addition as follows:
    7 X 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4
    (To keep the function simple, assume that x and y will always hold positive nonzero
    integers.)
"""
# define the main function
def main():
    # get our values
    val1 = int(input('Enter the first value to be multiplied: '))
    val2 = int(input('Enter the second value to be multiplied: '))
    sum = 0
    # pass the values to the function
    mult(val1, val2, sum)

# define mult()
def mult(x, y, sum):
    # if y is 0 just print the sum, which is 0
    if y == 0:
        print(sum)
    # if not then push it all back into the funtion but take 1 from y and add x to the sum
    else:
        return mult(x, y-1, sum + x)
# call main
main()


