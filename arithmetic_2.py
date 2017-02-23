def add(user_inputs):
    result = 0
    for num in user_inputs:
        result += num
    return result

def subtract(user_inputs):
    result = user_inputs[0]
    for num in user_inputs[1:]:
        result -= num
    return result

def multiply(user_inputs):
    result = 1
    for num in user_inputs:
        result *= num
    return result

def divide(user_inputs):
    # Need to turn at least argument to float for division to
    # not be integer division
    result = user_inputs[0]
    for num in user_inputs[1:]:
        result /= float(num)
    return result

def square(user_inputs):
    # Needs only one argument
    for num in user_inputs:
        result = num ** 2
    return result


def cube(user_inputs):
    # Needs only one argument
    for num in user_inputs:
        result = num ** 3
    return result

def power(user_inputs):
    result = user_inputs[0]
    for num in user_inputs[1:]:
        result = result ** num
    return result  # ** = exponent operator

def mod(user_inputs):
    result = user_inputs[0]
    for num in user_inputs[1:]:
        result = result % num
    return result
