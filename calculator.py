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
    try:
        input_split[1] = int(input_split[1])
        input_split[2] = int(input_split[2])
    except:
        pass
    if input_split[0] == "q":
        break
    else:
        if input_split[0] == "+":
            result = add(input_split[1], input_split[2])
        elif input_split[0] == "-":
            result = subtract(input_split[1], input_split[2])
        elif input_split[0] == "*":
            result = multiply(input_split[1], input_split[2])
        elif input_split[0] == "/":
            result = divide(input_split[1], input_split[2])
        elif input_split[0] == "square":
            result = square(input_split[1])
        elif input_split[0] == "cube":
            result = cube(input_split[1])
        elif input_split[0] == "pow":
            result = power(input_split[1], input_split[2])
        elif input_split[0] == "mod":
            result = mod(input_split[1], input_split[2])
        print result
