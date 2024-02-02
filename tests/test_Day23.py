# Test class for the Day23 challenge
# Write a program that checks if a key exists in a dictionary.

from challenges.Day23 import check_dictionary

# Test Cases :
# 1. Check if the dictionary is empty.
# 2. Check if the key to find is empty.
# 3. Check for the key exists in the dictionary.
# 4. Check for the key does not exist in the dictionary.


def test_check_dictionary():
    # TestCase 1:
    expected_result = 'Dictionary or key is empty'
    in_dict = {}
    assert expected_result == check_dictionary(in_dict,'a')
    # TestCase 2:
    expected_result = 'Dictionary or key is empty'
    in_dict = {'a': 12, 123: 'abc'}
    key_to_find = ''
    assert expected_result == check_dictionary(in_dict, key_to_find)
    # TestCase 3:
    expected_result = 'Found the key'
    in_dict = {'a': 12, 123: 'abc'}
    key_to_find = 123
    assert expected_result == check_dictionary(in_dict, key_to_find)
    # TestCase 4:
    expected_result = "Couldn't find the key"
    in_dict = {'a': 12, 123: 'abc'}
    key_to_find = 'b'
    assert expected_result == check_dictionary(in_dict, key_to_find)