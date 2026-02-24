# Yurt_Calculator_V1
Author: Will Yurt
Class: Engineering and Problemsolving
Python Unit

Project: Basic Multi-Function Calculator

Purpose: To do basic arithmetic. Can add, subtract, multiply, divide, evaluate exponents, modulo, and floor division.

Has 7 different defined functions. In the master loop , user selects a function via the if, elif, else satements, then is prompted to input their first (1st) and second (2nd) numbers for variables "a", "b" respectively. 
Uses variables "a", "b" as arguments. Runs the operation, saving the result in the variable "result", and prints the value of the variable "result"

Selected Criteria:

    (1) Master "while" loop for your code that accepts and uses user input.
        (a) Begins a while loop that runs on the condition where it checks if quit_statement != "quit"
    (2) Create your own functions (at least 2) and call every function that you made
        (a) Code has seven (8) different functions
        (b) Each function runs a different operation.
        (c) Function calling is ran off of user input.
        (d) One function collects the numbers of the user, returns the numbers in a tuple
    (3) Use error/exception handling and handles at least two types of error.
        (a) InputValueError
            - Handles when the user inputs a non number into the get_numbers function
        (b) ZeroDivisionError
            - Handles when the user attempts to divide by zero (0) when the functions that involve division are called.
            - Only activates if the variable "b" = 0 and the one of the division functions is called.


The test.py file is a proof of concept for having two separate main loops that can be selected between.

Calc_V1.5.py is the main file for the regex driven PEMDAS calculator
