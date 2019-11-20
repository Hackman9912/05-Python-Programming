"""
4. Largest List Item
    Design a function that accepts a list as an argument, and returns the largest value in the list.
    The function should use recursion to find the largest item.
"""
# Define main
def main():
    # Establish the list and variables
    list1 = [100,225,63,31529,99,85]
    count = 0
    big = 0
    # pass all to the function
    largest(list1, count, big)
# define the largest function
def largest(x, y, big):
    # if y is the same as the length of the list then print the value of big
    if y == len(x):
        print(big)
    # if not then see if big is bigger then the selected item on the list
    else:
        if big <= x[y]:
            # if it is then big equals that number
            big = x[y]
        # call the function again passing all the things and setting the counter plus 1
        return largest(x, y + 1, big)

main()