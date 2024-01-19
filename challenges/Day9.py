# Write a program to check if a number is even or odd.

# Steps:
# 1. Evaluate if the number is greater than 0 and type int
# 2. If not of type int throw an exception
# 3. If type is int, check for odd condition num%2==1 return 'odd' else 'even'

# Tests:
# 1. Check for if the number is greater than 0 if not print 'Invalid Number' message.
# 2. Check for the TYPE if not int throw an exception.
# 3. Check for valid number and print odd or even.


def evaluate_odd_even(processing_input):
    result = ''
    try:
        input_number = int(processing_input)
        if input_number > 0:
            if input_number % 2 == 1:
                result = 'Odd'
            else:
                result = 'Even'
        else:
            result = 'Invalid number'
    except ValueError:
        print('Incorrect type of number')
    return result


if __name__ == '__main__':
    print(evaluate_odd_even(input('Enter a number to evaluate odd or even : ')))


# Sample Output
# Enter a number to evaluate odd or even : 46
# Even
