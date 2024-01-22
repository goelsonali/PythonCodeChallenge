# Write a program to reverse a given string.
from functools import reduce


# Tests Cases:
# 1. Test for an empty string.
# 2. Test string with spaces.
# 3. Test string with no spaces.


def reverse_string(input_string):
    if input_string:
        list_str = input_string.split()
        result = ' '.join(list_str[::-1])
        return result
    else:
        return 'It is an empty string'


if __name__ == '__main__':
    print(f'Reversed string is : {reverse_string(input("Enter a string : "))}')


# Sample output
# Enter a string : happy days
# Reversed string is : days happy
