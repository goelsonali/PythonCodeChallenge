# Test class for the challenge Day34
# Write a Python program to merge two dictionaries.

from challenges.Day34 import merge_dic

# Test Cases -
# 1. Check for dictionaries if both are empty.
# 2. Check if 1 dictionary is empty.
# 3. Check for correct merged dictionary. (Consider each dictionary is distinct)


def test_merge_dic():
    # Test 1 :
    expected_result = 'The input dictionaries are empty'
    dict1 = {}
    dict2 = {}
    assert expected_result == merge_dic(dict1, dict2)

    # Test 2 :
    dict1 = {'p': 1, 'y': 2, 'python': 'today' }
    dict2 = {}
    merged_dict = {'p': 1, 'y': 2, 'python': 'today'}
    assert merged_dict == merge_dic(dict1, dict2)
    dict1 = {}
    dict2 = {1: 'p', 2: 'y'}
    merged_dict = {1: 'p', 2: 'y'}
    assert merged_dict == merge_dic(dict1, dict2)

    # Test 3 :
    dict1 = {'p': 1, 'y': 2, 'python': 'today' }
    dict2 = {1: 'p', 2: 'y'}
    merged_dict = {'p': 1, 'y': 2, 'python': 'today', 1: 'p', 2: 'y'}
    assert merged_dict == merge_dic(dict1, dict2)