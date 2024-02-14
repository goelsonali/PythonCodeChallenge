# Write a simple unit test for a function that adds two numbers


def add_numbers(num1, num2):
    result = 0
    if (isinstance(num1, int) or isinstance(num1, float)) and (isinstance(num2, int) or isinstance(num2, float)):
        result = num1 + num2
    elif isinstance(num1, str) and not isinstance(num2, str):
        result = float(num1) + num2
    elif not isinstance(num1, str) and isinstance(num2, str):
        result = num1 + float(num2)
    else:
        result = float(num1) + float(num2)
    return result
