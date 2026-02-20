'''
Will be a different function calculator to figure out how to have the user input an expression to be calculated
Likely will run off of regex
Will be implemented into Calc_V1.0 as V2.0
'''

import re

txt_to_search = "34567890/60"

operators_search = re.compile(r'[+\-*/%]')
operators = operators_search.finditer(txt_to_search)


num_search = re.compile(r'\d') #searches for single digits

#num_search = re.compile(r'\d\d')  #searches for 2 numbers in a row
#num_search = re.compile(r'\d\d\d')  #searches for 3 numbers in a row
#num_search = re.compile(r'\d\d\d\d')  #searches for 4 numbers in a row
#num_search = re.compile(r'\d\d\d\d\d')  #searches for 5 numbers in a row
#num_search = re.compile(r'\d\d\d\d\d\d')  #searches for 6 numbers in a row

numbers = num_search.finditer(txt_to_search)

#code below shows that it is working to me, will be removed later
#need to figure out how to index numbers and operators.
print('\nOperators')
for match in operators:
    print (match)
print('')

print ('Numbers')
for i in numbers:
    print (i)
print('')