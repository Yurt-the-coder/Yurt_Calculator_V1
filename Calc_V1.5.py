'''
Will be a different function calculator to figure out how to have the user input an expression to be calculated
Likely will run off of regex
Will be implemented into Calc_V1.0 as V2.0
'''

import re

txt_to_search = "34+1*5"

operators_search = re.compile(r'[+\-*/%]')

operators = operators_search.finditer(txt_to_search)

num_search = re.compile(r'\d')

numbers = num_search.finditer(txt_to_search)

print('\nOperators')
for match in operators:
    print (match)
print('')

print ('Numbers')
for i in numbers:
    print (i)
print('')