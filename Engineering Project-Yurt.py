""" General Info
Author: Will Yurt
Class: Engineering & Problemsolving
Project: Basic multi-function calculator

For more detail, see READ_ME
"""

#--------Functions----------------------------------------------------------------------------------

#Addition
def add (a, b):
    sum = a + b
    return sum

#Subtraction
def sub (a, b):
    difference = a - b
    return difference

#Multiplication
def mult (a, b):
    product = a * b
    return product

#Division
def div (a, b):
    quotient = a / b
    return quotient

#Exponents
def exponent (a, b):
    result = a ** b
    return result

#Modulo
def mod (a,b):
    result = a % b
    return result

#Floor Division
def floor_div (a,b):
    result = a // b
    return result

#Long Division function
def long_division (a,b):
    flr_quotient = floor_div (a,b)
    mod_result = mod (a,b)
    return flr_quotient, mod_result

#---------------------Main Loop------------------------------------------------------------------

quit_statement = ""

print ("Welcome to Will's Calculator 1.0 \n ")

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


    #inputs a string, tells what the if->elif->lse statement what to do
    function_selector = input("input selection: ")


    #checks the value of the string variable function_selector, main if statement is for addition
    #elif statements are for the rest of the functions
    #else is to let the user know they put a mis-input
    try:
        if function_selector == "+": #addition function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            sum = add (a, b)
            print(sum)

        elif function_selector == "-": #subtraction function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            difference = sub (a, b)

        elif function_selector == "*": #multiplication function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            product = mult (a, b)

        elif function_selector == "/": #regular division function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            quotient = div (a, b)

        elif function_selector == "**": #exponent function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            result = exponent (a, b)
            
        elif function_selector == "//": #floor division function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            result = floor_div (a,b)
            
        elif function_selector == "%": #modulo function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            result = mod (a,b)

        elif function_selector == "//%": #long division function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            long_div_answer = long_division (a, b) #returns as a tuple
            print(long_div_answer[0], ", Remainder = ", long_div_answer[1])
                #Index [0] in the tuple will be flr_quotient
                #Index [1] in the tuple will be mod_result

        else: #activates when the user does not use one of the specififed inputs
            print("please input a specified input to select function")
            continue #returns to the top of the loop
    
    except ValueError: #handles if the user does not input a number for 'a' or 'b'
        print ("please input a number, ex, 1 or 54.3, ect.")
        continue

    except ZeroDivisionError: #handles if user attemots to divide by zero
        print("Cannot divide by Zero, is UNDEFINED or DOES NOT EXIST")
        continue

    quit_statement = input("to end, input quit; else put continue: ")
    print ()
    
    if quit_statement == "quit":
        print ("Goodbye \n")
    #end of main loop
