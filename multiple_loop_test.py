#proof for the multi loop idea for V2.0
#contains the addition functionality from Calc V1.0
#code will be used to build V2.0 when V1.5 is complete
#V2.0 will be a combination of V1.0 and V1.5 into two selectable loops and a main menu.

#--------Functions---------------------------------------------------------------------------------

#Addition.
def add (a, b):
    sum = a + b
    return sum


#---------------------Main Loop--------------------------------------------------------------------

quit_statement = ""
quit_statement_2 = ""

calc_selector_and_quit = ""

print("Welcome to Will's Calculator 1.0")
while calc_selector_and_quit != "quit":
    calc_selector_and_quit = input("input V1.5 for 2, inpput 'V1.0' for original, input 'quit' to quit ")
    if calc_selector_and_quit == "V1.0":
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
            function_selector = input("input selection: ")
            try:
                if function_selector == "+": #addition function selector
                    a = float(input("input first number: "))
                    b = float(input("input second number: "))
                    sum = add (a, b)
                    print('\n', sum, '\n')
            except ValueError: #handles if the user does not input a number for 'a' or 'b'
                print ("please input a number, ex, 1 or 54.3, ect.")
                continue

            except ZeroDivisionError: #handles if user attemots to divide by zero
                print("Cannot divide by Zero, is UNDEFINED or DOES NOT EXIST")
                continue

            quit_statement = input("to end, input quit; else put continue: ")
            quit_statement = quit_statement.lower()
            print("")
    
            if quit_statement == "quit":
                print ("Goodbye!")
            #end of loop
    if calc_selector_and_quit == "V1.5":
        while quit_statement_2 != "quit":
            print ("v2")
            quit_statement_2 = input("'quit' to return to main ")
            quit_statement_2 = quit_statement_2.lower()