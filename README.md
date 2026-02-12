# Yurt_Calculator_V1
Author: Will Yurt
Class: Engineering and Problemsolving
Python Unit

Project: Basic Multi-Function Calculator

Purpose: To do basic arithmetic. Can add, subtract, multiply, divide, evaluate exponents, modulo, and floor division.

Has 7 different defined functions. Each one begins with asking for input for the variables "a" and "b". Runs the operation, saving the result in the variable "result", and prints the value of the variable "result"

Selected Criteria:

    (1) Master "while" loop for your code that accepts and uses user input.
        (a) Begins a while loop that runs on the condition where it checks if quit_statement != "quit"
    (2) Create your own functions (at least 2) and call every function that you made
        (a) Code has seven (7) different functions
        (b) Each function runs a different operation.
        (c) Function calling is ran off of user input.
    (3) Use error/exception handling and handles at least two types of error.
        (a) InputValueError
            - Concerns variable "a" and variable "b"
            - Variable "a" is the first number in all of the functions
                - Ex) the dividend and minuend
            - Variable "b" is the second number in all of the functions
                - Ex) the divisor and subtrahend
        (b) ZeroDivisionError
            - Handles when the user attempts to divide by zero when the functions that involve division are called.
            - Only activates if the variable "b" = 0 and the one of the division functions is called.
