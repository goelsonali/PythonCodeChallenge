# Create a program to find the largest among three numbers.

# Test Cases
# 1. Check if the type of input is int if not throw an error.
# 2. Check with input as int type.
# 3. Check if input is empty.


def max_number(process_input):
    try:
        if process_input:
            input_numbers = (int(x) for x in process_input)
            return max(input_numbers)
        else:
            return 'No input'
    except ValueError:
        print('The input is not a number')
        return 'Not valid type of input'


if __name__ == '__main__':
    input1 = input('Enter 1st number:')
    input2 = input('Enter 2nd number:')
    input3 = input('Enter 3rd number')
    input_to_process = [input1, input2, input3]
    print(max_number(input_to_process))


# Sample output
# Enter 1st number:1
# Enter 2nd number:34
# Enter 3rd number23
# 34

# Enter 1st number:abc
# Enter 2nd number:12
# Enter 3rd numbere
# The input is not a number
# Not valid type of input

