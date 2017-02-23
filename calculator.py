"""# No setup
repeat forever:
    read input
    tokenize input
    if the first token is 'q'
        quit
    else
        decide which math function to call based on first token
"""
"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    input = raw_input()
    input_split = input.split(" ")
    if input_split[0] == "q":
        break
    else:
        if input_split[0] == "+":
            add(input_split[1], input_split[2])
        elif input_split[0] == "-":
            subtract(input_split[1], input_split[2])
        elif input_split[0] == "*":
            multiply(input_split[1], input_split[2])
        elif input_split[0] == "/":
            divide(input_split[1], input_split[2])
        elif input_split[0] == "square":
            square(input_split[1])
        elif input_split[0] == "cube":
            cube(input_split[1])
        elif input_split[0] == "pow":
            power(input_split[1], input_split[2])
        elif input_split[0] == "mod":
            mod(input_split[1], input_split[2])
