# Write a program to iterate through a dictionary and print its keys and values.
import itertools


def dictionary_using_for_loop(input_dict):
    if input_dict:
        for key, value in input_dict.items():
            print(f'key : {key}, value: {value}')


def dictionary_using_itertools(input_dict1, input_dict2):
    if input_dict1 or input_dict2:
        for key, value in itertools.chain(input_dict1.items(), input_dict2.items()):
            print(f'key : {key}, value: {value}')


if __name__ == '__main__':
    input_dict1 = {'a': 1, 'b': 2}
    input_dict2 = {'c': 3, 'd': 4}
    print('Using Simple For Loop')
    dictionary_using_for_loop(input_dict1)
    print('Using itertools library')
    dictionary_using_itertools(input_dict1, input_dict2)


# Sample output
# Using Simple For Loop
# key : a, value: 1
# key : b, value: 2
# Using itertools library
# key : a, value: 1
# key : b, value: 2
# key : c, value: 3
# key : d, value: 4

