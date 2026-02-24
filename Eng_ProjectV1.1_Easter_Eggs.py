import time

#--------Functions---------------------------------------------------------------------------------

#get_nums
def get_numbers ():
    num_1 = float(input("input first number: "))
    num_2 = float(input("input second number: "))
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

#---------------------Main Loop--------------------------------------------------------------------

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


    #inputs a string, tells what the if->elif->lse statement what to do
    function_selector = input("input selection: ")
    
    #easter eggs
    if function_selector == 'hello there':
        print("\nGeneral Kenobi, cough, cough.\nYou are a bold one.\n")
        time.sleep(3)
    elif function_selector == 'Hello there':
        print("\nGeneral Kenobi, cough, cough.\nYou are a bold one.\n")
        time.sleep(3)
    elif function_selector == "my new empire":
        print("\nObi-wan: You have allowed this dark lord to twist your mind, \nuntil now you've become the very thing you swore to destroy.\n")
        time.sleep(1.5)
        print("Anakin: Don't lecture me Obi-Wan! I see through the lies of the Jedi.\n")
        time.sleep(2)
        print("        I do not fear the dark side as you do.")
        time.sleep(1)
        print("\n        I have brought peace freedom, justice and security to my new Empire.\n")
        time.sleep(3)
        print("Obi-wan: Your new Empire?\n")
        time.sleep(1.5)
        print("Anakin: Don't make me kill you.\n")
        time.sleep(1.5)
        print("Obi-wan: Anakin, my allegiance is to the Republic, to democracy.\n")
        time.sleep(1.5)
        print("Anakin: if you're not with me, then you're my enemy.\n")
        time.sleep(1.5)
        print("Obi-Wan: Only a Sith deals in abslutes. I will do what I must.\n")
        time.sleep(1)
        print("Anakin: You will try.\n\n\n")
        time.sleep(3)
        print("All credit given to George Lucas for the Star Wars quotes\n\n\n\n")
    #all credit is to George Lucas for the Star Wars quotes

    #checks the value of the string variable function_selector, main if statement is for addition
    #elif statements are for the rest of the functions
    #else is to let the user know they put a mis-input
    try:
        if function_selector == "+": #addition function selector
            numbers = get_numbers()
            sum = add (numbers[0], numbers[1])
            print('\n', sum, '\n')

        elif function_selector == "-": #subtraction function selector
            numbers = get_numbers()
            difference = sub (numbers[0], numbers[1])
            print('\n', difference, '\n')

        elif function_selector == "*": #multiplication function selector
            numbers = get_numbers()
            product = mult (numbers[0], numbers[1])
            print('\n', product, '\n')

        elif function_selector == "/": #regular division function selector
            numbers = get_numbers()
            quotient = div (numbers[0], numbers[1])
            print('\n', quotient, '\n')

        elif function_selector == "**": #exponent function selector
            numbers = get_numbers()
            exp_result = exponent (numbers[0], numbers[1])
            print('\n',exp_result, '\n')
            
        elif function_selector == "//": #floor division function selector
            numbers = get_numbers()
            flr_div_result = floor_div (numbers[0], numbers[1])
            print('\n', flr_div_result, '\n')
            
        elif function_selector == "%": #modulo function selector
            numbers = get_numbers()
            mod_result = mod (numbers[0], numbers[1])
            print('\n', mod_result, '\n')

        elif function_selector == "//%": #long division function selector
            numbers = get_numbers()
            long_div_answer = long_division (numbers[0], numbers[1]) #returns as a tuple
            print('\n', int(long_div_answer[0]), ", Remainder = ", int(long_div_answer[1]), '\n')
                #Index [0] in the tuple will be flr_quotient of the long_division function
                #Index [1] in the tuple will be mod_result of the long_division function
        
        #developer tool, breaks the code early
        elif function_selector == "quit":
            break
        elif function_selector == "break":
            break

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
    quit_statement = quit_statement.lower()
    print("")
    
    if quit_statement == "quit":
        print ("Goodbye!")
    #end of main loop