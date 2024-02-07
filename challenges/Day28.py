# Create a program that removes the nth element from a list.

# Test Cases :
# 1. Check if the list is empty.
# 2. Check if the nth record is valid.
# 3. Check for correct nth record removal.


def remove_nth_record(input_list_processing, n):
    if input_list_processing and n < len(input_list_processing):
        input_list_processing.remove(input_list_processing[n])
        return input_list_processing
    else:
        return 'The list is empty or nth index is incorrect'


in_list = [1, 4, 6, 'string', 'python']
n = 2
print(f'The input string - {in_list} to remove {n}th element. Processed list now {remove_nth_record(in_list, n)}')
n = -1
print(f'The input string - {in_list} to remove {n}th element. Processed list now {remove_nth_record(in_list, n)}')

# Sample output :
# The input string - [1, 4, 6, 'string', 'python'] to remove 2th element. Processed list now [1, 4, 'string', 'python']
# The input string - [1, 4, 'string', 'python'] to remove -1th element. Processed list now [1, 4, 'string']

