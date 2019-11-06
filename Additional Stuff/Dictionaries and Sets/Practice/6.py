'''
6. File Analysis
Write a program that reads the contents of two text files and compares them in the 
following ways:
• It should display a list of all the unique words contained in both files.
• It should display a list of the words that appear in both files.
• It should display a list of the words that appear in the first file but not the 
second.
• It should display a list of the words that appear in the second file but not the 
first.
• It should display a list of the words that appear in either the first or second file 
but not both.
Hint: Use set operations to perform these analyses.
'''

def main():
    set1 = set()
    set2 = set()
    file_set('fileset1.txt', set1)
    file_set('fileset2.txt', set2)
    set3 = set1 | set2
    print("Here is a list of unique words from both files", set3)
    set4 = set1 & set2
    print("Here are the words that appear in both files: ", set4)
    unique1 = set1.difference(set2)
    print("Here are the words that appear in file 1 only: ", unique1)
    unique2 = set2.difference(set1)
    print("Here are the words that appear in file 2 only: ", unique2)
    unique3 = set1 ^ set2
    print("Here are the words that appear in one file or the other but not both: ", unique3)

def file_set(file_name, word_set):
    # open the file
    with open(file_name, 'r') as f:
        # iterate through the file
        for line in f:
            # split up each word
            for word in line.split():
                # add the word to the set
                word_set.add(word)
    # display the set
    # print("Here are the words from", file_name, " ", word_set)


main()