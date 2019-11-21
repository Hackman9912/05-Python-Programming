"""
4. Match the set of all valid Python identifiers.
"""
import re
text = '''
Manpower
manpower
_manpower
myClass
var_1
1var
'''
pattern = re.compile(r'\b[a-zA-Z_][a-zA-Z_0-9]+\b')
matches = pattern.finditer(text)
for match in matches:
    print(match)