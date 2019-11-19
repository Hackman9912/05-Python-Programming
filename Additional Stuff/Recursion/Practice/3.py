"""
3. Recursive Lines
    Write a recursive function that accepts an integer argument, n. The function should display
    n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line
    showing 2 asterisks, up to the nth line which shows n asterisks.
"""

def stuff():
    list = []
    y = 1
    ast = int(input('Enter the number of asterisk and lines that you want to see: '))
    lines(ast, list, y)

def lines(x, list, y):
    if x == 0:
        print(*list, sep = '\n')
    else:
        list.append('*' * y)
        return lines(x - 1, list, y + 1)


stuff()