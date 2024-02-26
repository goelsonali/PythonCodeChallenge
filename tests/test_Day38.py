# Write a program to flatten a nested list.

from challenges.Day38 import with_for_loop_flatten_list, with_comprehension_flatten_list

# Test Cases
# 1. Check if nested_input list is empty.
# 2. Check if list is nested.


def test_for_anagram():
    # Test 1 :
    nested_input = []
    expected_result = []
    assert expected_result == with_for_loop_flatten_list(nested_input)
    
    # Test 2 :
    nested_input = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    expected_result = ['a', 'b', 'c', 'd', 'e', 'f']
    assert expected_result == with_for_loop_flatten_list(nested_input)
    assert expected_result == with_comprehension_flatten_list(nested_input)
