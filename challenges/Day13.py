# Write a program to shuffle the elements of a list randomly.

import random

# Test Cases:
# 1. For an empty list.
# 2. For mixed type of data.


def shuffle_elements(input_list):
    if input_list:
        random.shuffle(input_list)
        return input_list
    else:
        return 'List is empty'


if __name__ == '__main__':
    in_list = ['py', 'now', 'call']
    print(f'List before reshuffle : {in_list}')
    print(f'After reshuffle : {shuffle_elements(in_list)}')

# Sample output
# List before reshuffle : ['py', 'now', 'call']
# After reshuffle : ['call', 'py', 'now']

