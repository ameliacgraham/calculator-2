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
    # Get user input and splice it into a list where there is a space
    user_input = raw_input()
    tokens = user_input.split(" ")
    operator = tokens[0]
    
    # If there is a second and third value, converts them into integers
    try:
        tokens[1] = int(tokens[1])
        tokens[2] = int(tokens[2])
    except IndexError:
        pass
    except ValueError:
        print "Invalid entry"
        continue

    # Allows the user to quit
    if operator == "q":
        break
    # Calls each function depending on the operator
    else:
        if operator == "+":
            result = add(tokens[1], tokens[2])
        elif operator == "-":
            result = subtract(tokens[1], tokens[2])
        elif operator == "*":
            result = multiply(tokens[1], tokens[2])
        elif operator == "/":
            result = divide(tokens[1], tokens[2])
        elif operator == "square":
            result = square(tokens[1])
        elif operator == "cube":
            result = cube(tokens[1])
        elif operator == "pow":
            result = power(tokens[1], tokens[2])
        elif operator == "mod":
            result = mod(tokens[1], tokens[2])
        else:
            print "Invalid entry"
            continue

        print result
