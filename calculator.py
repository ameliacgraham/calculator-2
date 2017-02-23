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

from arithmetic_2 import *

while True:
    # Get user input and splice it into a list where there is a space
    user_input = raw_input()
    tokens = user_input.split(" ")
    operator = tokens[0]
    numbers = []
    
    # If there is a second and third value, converts them into integers
    try:
        for num in tokens[1:]:
            numbers.append(int(num))
    except ValueError:
        print "Invalid entry"
        continue

    # Allows the user to quit
    if operator == "q":
        break
    # Calls each function depending on the operator
    else:
        if operator == "+":
            result = add(numbers)
        elif operator == "-":
            result = subtract(numbers)
        elif operator == "*":
            result = multiply(numbers)
        elif operator == "/":
            result = divide(numbers)
        elif operator == "square":
            result = square(numbers)
        elif operator == "cube":
            result = cube(numbers)
        elif operator == "pow":
            result = power(numbers)
        elif operator == "mod":
            result = mod(numbers)
        else:
            print "Invalid entry"
            continue

        print result
