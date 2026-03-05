""" General Info
Author: Will Yurt
Class: Engineering & Problemsolving
Project: Basic multi-function calculator

For more detail: see READ_ME
"""

#--------Functions---------------------------------------------------------------------------------

#get_nums
def get_numbers ():
    num_1 = float(input("Input first number: "))
    print("")
    num_2 = float(input("Input second number: "))
    print("")
    return num_1, num_2

#Addition
def add (a, b):
    sum = a + b
    return sum

#Subtraction
def sub (a, b):
    difference = float(a - b)
    return difference

#Multiplication
def mult (a, b):
    product = float(a * b)
    return product

#Division
def div (a, b):
    quotient = float(a / b)
    return quotient

#Exponents
def exponent (a, b):
    result = float(a ** b)
    return result

#Modulo
def mod (a,b):
    mod_result = (a % b)
    return mod_result

#Floor Division
def floor_div (a,b):
    flr_result = (a // b)
    return flr_result

#Long Division function
def long_division (a,b):
    flr_quotient = floor_div (a,b)
    mod_result = mod (a,b)
    return flr_quotient, mod_result


#---------------------Main_Loop--------------------------------------------------------------------
quit_statement = ""

print("Welcome to Will's Calculator 1.0\n")

while quit_statement != "quit":
    #table showing what the inputs to select each function are
    print("Inputs to Select Functions \n")
    print("   for addition input:         |  +")
    print("   for subtraction input:      |  -")
    print("   for multiplication input:   |  *")
    print("   for regular division input: |  /")
    print("   for exponent input:         |  **")
    print("   for Floor Division input:   |  //")
    print("   for Modulo input:           |  %")
    print("   for Long Division input:    |  //% \n")
    function_selector = input("input selection: ")  #inputs a string, tells what the if->elif->lse statement what to do
    print("")
    #checks the value of the string variable function_selector, main if statement is for addition
    #elif statements are for the rest of the functions
    #else is to let the user know they put a mis-input
    try:
        if function_selector == "+": #addition function selector
            numbers = get_numbers()
            sum = add (numbers[0], numbers[1])
            print('\nSum is:', sum, '\n')

        elif function_selector == "-": #subtraction function selector
            numbers = get_numbers()
            difference = sub (numbers[0], numbers[1])
            print('\nDifference is:', difference, '\n')

        elif function_selector == "*": #multiplication function selector
            numbers = get_numbers()
            product = mult (numbers[0], numbers[1])
            print('\nProduct is:', product, '\n')

        elif function_selector == "/": #regular division function selector
            numbers = get_numbers()
            quotient = div (numbers[0], numbers[1])
            print('\nQuotient is:', quotient, '\n')

        elif function_selector == "**": #exponent function selector
            numbers = get_numbers()
            exp_result = exponent (numbers[0], numbers[1])
            print('\nAnswer is:',exp_result, '\n')
            
        elif function_selector == "//": #floor division function selector
            numbers = get_numbers()
            flr_div_result = floor_div (numbers[0], numbers[1])
            print('\nAnswer is:', flr_div_result, '\n')
            
        elif function_selector == "%": #modulo function selector
            numbers = get_numbers()
            mod_result = mod (numbers[0], numbers[1])
            print('\nAnswer is:', mod_result, '\n')

        elif function_selector == "//%": #long division function selector
            numbers = get_numbers()
            long_div_answer = long_division (numbers[0], numbers[1]) #returns as a tuple
            print(f'\nAnswer is: {int(long_div_answer[0])} Remainder = {int(long_div_answer[1])} \n')
                #Index [0] in the tuple will be flr_quotient of the long_division function
                #Index [1] in the tuple will be mod_result of the long_division function
        
        #--------------------------------------
        #developer tool, breaks the code early
        elif function_selector == "quit":
            break
        elif function_selector == "break":
            break
        #--------------------------------------

        else: #activates when the user does not use one of the specififed inputs [+, -, *, /, **, %, //%]
            print("\n--------------------------------------------------")
            print("ERROR: INVALID CHARACTER(s) INPUT\nplease input a specified input to select function")
            print("--------------------------------------------------\n")
            continue #returns to the top of the loop

    #---------------------------------------------------------------------------------------------------------------
    #EXCEPTION HANDLING    
    except ValueError: #activates if the user does not input a number for 'a' or 'b' in the get_nums function
        print("\n--------------------------------------------------")
        print ("ERROR: INVALID CHARACTER(s) INPUT\nplease input a number, ex, 1 or 54.3, ect.")
        print("--------------------------------------------------\n")
        continue

    except ZeroDivisionError: #handles if user attempts to divide by zero
        print("\n--------------------------------------------------")
        print("ERROR: ZERO DIVISION ERROR\nCannot divide by Zero, is UNDEFINED or DOES NOT EXIST")
        print("--------------------------------------------------\n")
        continue
    #---------------------------------------------------------------------------------------------------------------


    quit_statement = input("to end, input quit; else put continue: ")
    quit_statement = quit_statement.lower()
    print("")
    
    if quit_statement == "quit":
        print ("Goodbye!")
        break
#----------------------------------end of main loop---------------------------------------------------------------------------------------------------------------------------