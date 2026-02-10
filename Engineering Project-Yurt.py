"""
Author: Will Yurt
Class: Engineering & Problemsolving
Project: multi-function calculator
Criteria
    1)
    2)
    3)

"""
#Functions----------------------------------------------------------------------------------

#Addition
def add (a, b):
    sum = a + b
    print (sum)

#Subtraction
def sub (a, b):
    difference = a - b
    print (difference)

#Multiplication
def mult (a, b):
    product = a * b
    print (product)

#Division
def div (a, b):
    quotient = a / b
    print (quotient)

#Exponents
def exponent (a, b):
    result = a ** b
    print (result)

#Modulo
def mod (a,b):
    result = a % b
    print (result)

#Floor Division
def floor_div (a,b):
    result = a // b
    print (result)

#Long Division (Floor Division and Modulo)
def long_division (a, b):
    Floor_Quotient = a // b
    Mod = a % b
    print(Floor_Quotient , "R=",Mod)


#--------------------------------------------------------------------------------------------

#Main Loop
quit_statement = ""

print ("Welcome to Will's Calculator 1.0")
while quit_statement != "quit":

    #input table to tell user how select functions
    print("Inputs to Select Functions")
    print("    for addition input:         +")
    print("    for subtraction input:      -")
    print("    for multiplication input:   *")
    print("    for regular division input: /")
    print("    for exponent input:         **")
    print("    for Floor Division input:   //")
    print("    for Modulo input:           %")
    print("    for Long Division input:    //%")

#inputs a string, tells what the if->elif->lse statement what to do
    function_selector = input("input selection: ")

#checks the value of the string variable function_selector, main if statement is for addition
#elif statements are for the rest of the functions
#else is to let the user know they put a mis-input
    try:
        
        if function_selector == "+": #addition function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            add (a, b)

        elif function_selector == "-": #subtraction function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            sub (a, b)

        elif function_selector == "*": #multiplication function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            mult (a, b)

        elif function_selector == "/": #regular division function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            div (a, b)

        elif function_selector == "**": #exponent function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            exponent (a, b)

        elif function_selector == "//": #floor division function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            floor_div (a,b)

        elif function_selector == "%": #modulo function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            mod (a,b)

        elif function_selector == "//%": #long division function selector
            a = float(input("input first number: "))
            b = float(input("input second number: "))
            long_division (a, b)
            
        else: #activates when the user does not use one of the specififed inputs
            print("please input a specified input to select function")
            continue #returns to the top of the loop
    
    except ValueError: #handles if the user does not input a number for 'a' or 'b'
        print ("please input a number")
        continue

    except ZeroDivisionError: #handles if user attemots to divide by zero
        print("Cannot divide by Zero")

    quit_statement = input("to end, input quit; else put continue: ")