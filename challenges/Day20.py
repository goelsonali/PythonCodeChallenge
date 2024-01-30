# Write a function that takes a list of numbers and returns a new list containing only the even numbers.

# Test Cases :
# 1. Check for an empty list return relevant message.
# 2. Check for list elements only even numbers.
# 3. Check for list elements mixed(even and odd) numbers.
# 4. Check for list with mixed type.


def get_list_even(list_to_process):
    if list_to_process:
        result = [x for x in list_to_process if isinstance(x, int) and x % 2 == 0]
        return result
    else:
        return 'Input list is empty'


if __name__ == '__main__':
    input_list = [5.1, 2.0, 4, 28, 'a', 'b']
    print(f'Resulted list : {get_list_even(input_list)}')

# Sample output:
# Resulted list : [4, 28]
