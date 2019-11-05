'''
4. Unique Words
Write a program that opens a specified text file and then displays a list of all the unique
words found in the file.
Hint: Store each word as an element of a set
'''

unique_file = open('unique.txt', 'r')

line = unique_file.readline()

print(line)