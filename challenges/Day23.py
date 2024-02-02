# Write a program that checks if a key exists in a dictionary.

# Test Cases :
# 1. Check if the dictionary is empty.
# 2. Check if the key to find is empty.
# 3. Check for the key exists in the dictionary.
# 4. Check for the key does not exist in the dictionary.


def check_dictionary(dictionary_to_process, key_to_find):
    if dictionary_to_process and key_to_find:
        if dictionary_to_process.get(key_to_find):
            return "Found the key"
        else:
            return "Couldn't find the key"

    else:
        return 'Dictionary or key is empty'


if __name__ == '__main__':
    dictionary_to_check = {'a': 1, 'b': 2, 'c': 3}
    key_to_check = 'a'
    print(f'Check if the key - "{key_to_check}" exist in dictionary - {dictionary_to_check} '
          f'\n{check_dictionary(dictionary_to_check, key_to_check)}')

# Sample output :
# Check if the key - "a" exist in dictionary - {'a': 1, 'b': 2, 'c': 3}
# Found the key
