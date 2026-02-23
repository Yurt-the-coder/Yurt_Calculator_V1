'''
Will be a different function calculator to figure out how to have the user input an expression to be calculated
Likely will run off of regex
Will be implemented into Calc_V1.0 as V2.0
'''


#imports regex
import re

#text that I am searching, for testing purposes, will be run off user input later.

#txt_to_search = " 45 + 3"
txt_to_search = ' ' + input("input expression")
#Operators Search______________________________________________
operators_search = re.compile(r'[+\-*/%()]')

operators = operators_search.finditer(txt_to_search)


#Numbers Search________________________________________________
num_search = re.compile(r' [0-9]+') #searches for single digits

#num_search = re.compile(r'\d\d')          #searches for 2 numbers in a row
#num_search = re.compile(r'\d\d\d')        #searches for 3 numbers in a row
#num_search = re.compile(r'\d\d\d\d')      #searches for 4 numbers in a row
#num_search = re.compile(r'\d\d\d\d\d')    #searches for 5 numbers in a row
#num_search = re.compile(r'\d\d\d\d\d\d')  #searches for 6 numbers in a row

numbers = num_search.finditer(txt_to_search)

#code below shows that it is working to me, will be removed later
#need to figure out how to store the index of ops and nums
print('\nOperators')
for match in operators:
    print (match)
print('')

print ('Numbers')
for num in numbers:
    print (num)
print('')

