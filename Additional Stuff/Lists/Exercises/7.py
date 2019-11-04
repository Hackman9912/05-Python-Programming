"""
7. (Largest rows and columns) Write a program that randomly fills in 0s and 1s into
a matrix, prints the matrix, and finds the rows and columns with the most
1s. Here is a sample run of the program:
0011
0011
1101
1010
The largest row index: 2
The largest column index: 2, 3
"""
# Import the randomizer
import random

# Establish constants
ROWS = 4
COLUMNS = 4

# define main
def main():

    # Establish 2d list
    values = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    # Establish list for rows and columns
    row = []
    column = []

    # establish stick and count to count 1s in rows and columns
    count = 0
    stick = 0

    # Establish ticker and tic to keep track of the row
    tic = 0
    ticker = 0
    # Randomize the contents of values 
    for r in range(ROWS):
        for c in range(COLUMNS):
            values[r][c] = random.randint(0, 1)

# Print values for helping the solving
    print(values)
    
# walk through the rows
    for r in range(ROWS):
        ticker += 1
        if values[r] == 1:
            count += 1
        bigrows = values.index(r)
        if ticker == 3:
            row.append(count)
            ticker = 0
        for c in range(COLUMNS):
            tic += 1
            if value[c] == 1:
                stick += 1
            bigcolumns = values.index(c)
            if tic == 3:
                column.append(stick)
                tic = 0
    print(column)
    print(row)


main()