# Regular Expressions or RegEx

import re

text_to_match = '''lol
Daniel 1234 abcd
this.thing@email.com
this_otherthing@email.com
    there_was_a_tab
    210-444-4444
888*888*8888
lol
lol lololol
lol'''


# *************************************** String Literals ******************************************
'''print('\tTab')


# compile() will allow us to separate our pattern matches into a variable that makes it easier to reuse our variable
pattern = re.compile(r'1234')

# match()
# determines if the regex matches at the beginning of the string. Returns none if its not at beginning, sam as ^ anchor
match = pattern.match(text_to_match)
print(match)


# search() lets us search the entire string so it is better than match
search_item = pattern.search(text_to_match)
print(search_item)

# finditer()
pattern = re.compile(r'abcd')
matches = pattern.finditer(text_to_match)

for match in matches:
    print(match)'''


# ************************************** Meta Characters ****************************

'''
# . - the period or dot will find any character except new line
pattern = re.compile(r'.')
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# use . to find any character and \. to find any actual period or dot
pattern = re.compile(r'\.') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# \d finds any digits 0 to 9
pattern = re.compile(r'\d') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# The \D finds any non digit from 0 to 9
# Capitals essentially negate 
pattern = re.compile(r'\D') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# The \w finds any Word character (a-z, A-Z, 0-9 and _)
pattern = re.compile(r'\w') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# the \W finds any non Word characters.. the opposite of above
pattern = re.compile(r'\W') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# the \s finds any Whitespace (spaces, tabs, new lines)
pattern = re.compile(r'\s') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# the \S finds anything that is not space, tab or newline so similar to \w but has special characters
pattern = re.compile(r'\S') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)
'''

#**************************** Anchors ****************************************
# Anchors don't match characters but match invisible positions before or after characters
'''
# \b - finds word boundaries(anything prefixed with start of a new line, start of a string, tabs)
#  ie the spaces in front of the character. Use \b+the word that you want it to find. So \blol so finds the space in front of the word we search for and the word
pattern = re.compile(r'\blol') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# \B - finds nonword boundaries. So no spaces in between
pattern = re.compile(r'\Blol') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# ^ - finds matches at beginning of strings. Used as ^ + the text you want
pattern = re.compile(r'^lol') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# $ find matches at end of the string: used as the text you want + $
pattern = re.compile(r'lol$') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# Combining things
# find 3 numbers in a row
pattern = re.compile(r'\d\d\d') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)
'''
# find phone numbers
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)