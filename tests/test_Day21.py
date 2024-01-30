# Tests for the challenge Day21 -
# Create a program to remove a specific element from a set.

from challenges.Day21 import remove_element


# Test Cases:
# 1. Check for mixed type values.
# 2. Check for same type values.
# 3. Check for empty set.


def test_remove_element():
    # Test1 :
    expected_result_set = {'a', 'b', 1, 2, '5.0'}
    input_set = {'a', 'b', 1, 2, 'py', '5.0'}
    element_to_remove = 'py'
    assert expected_result_set == remove_element(input_set, element_to_remove)
    # Test2 :
    expected_result_set = {1, 2, 5, 10}
    input_set = {1, 2, 4, 5, 10}
    element_to_remove = 4
    assert expected_result_set == remove_element(input_set, element_to_remove)
    # Test3 :
    expected_result = 'The input set is empty'
    input_set = {}
    element_to_remove = 4
    assert expected_result == remove_element(input_set, element_to_remove)