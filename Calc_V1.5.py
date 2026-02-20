'''
Will be a different function calculator to figure out how to have the user input an expression to be calculated
Likely will run off of regex
Will be implemented into Calc_V1.0 as V2.0
'''

import re

txt_to_search = "1%2"

index = re.compile(r'[+\-*/%]')

matches = index.finditer(txt_to_search)

for match in matches:
    print (match)