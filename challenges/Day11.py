# Write a program to print the multiplication table of a given number.

# Test cases:
# 1. Check for O and 1 as input number.
# 2. Check for any number.
# 3. Check for any string/float type.

def print_multiplication_table(input_number):
    result = ''
    if isinstance(input_number, int):
        if input_number > 1:
            i = 1
            while i <= 10:
                result += f'{input_number} X {i}   = {input_number * i}\n'
                i += 1
        else:
            result = 'Enter number greater than 1'
    else:
        result = 'Incorrect input type'
    return result


if __name__ == '__main__':
    print(print_multiplication_table(12))
    print(print_multiplication_table('12'))

# Sample Output:
# 12 X 1   = 12
# 12 X 2   = 24
# 12 X 3   = 36
# 12 X 4   = 48
# 12 X 5   = 60
# 12 X 6   = 72
# 12 X 7   = 84
# 12 X 8   = 96
# 12 X 9   = 108
# 12 X 10   = 120
# Incorrect input type