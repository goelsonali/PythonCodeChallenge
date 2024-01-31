# Create a program to find the second-largest element in a list.

# Test Cases:
# 1. Check for a list with only int type.
# 2. Check for a list with only float type.
# 3. Check for a list with mixed int and float type.
# 4. Check for an empty list.


def find_second_largest(list_to_process):
    if list_to_process:
        list_to_process.sort()
        return list_to_process[-2]
    else:
        return 'Input list is empty'


if __name__ == '__main__':
    input_list = [1, 5, 3, 20, 34, 56, 10]
    print(f'The second-largest element in the list - {input_list} is {find_second_largest(input_list)}')
    input_list = [1, 5.0, 3, 20.3, 20.5, 56, 10]
    print(f'The second-largest element in the list - {input_list} is {find_second_largest(input_list)}')

# Sample Output
# The second-largest element in the list - [1, 5, 3, 20, 34, 56, 10] is 34
# The second-largest element in the list - [1, 5.0, 3, 20.3, 20.5, 56, 10] is 20.5

