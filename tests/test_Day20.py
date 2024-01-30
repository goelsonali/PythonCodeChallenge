# Tests for the challenge Day20 -
# Write a function that takes a list of numbers and returns a new list containing only the even numbers.

from challenges.Day20 import get_list_even

# Test Cases :
# 1. Check for an empty list return relevant message.
# 2. Check for list elements only even numbers.
# 3. Check for list elements mixed(even and odd) numbers.
# 4. Check for list with mixed type.


def test_get_list_even():
    # Test1:
    expected_result = 'Input list is empty'
    assert expected_result == get_list_even([])
    # Test2:
    expected_result = [2, 4, 20]
    input_list = [2, 4, 20]
    assert expected_result == get_list_even(input_list)
    # Test3:
    expected_result = [2, 4, 10, 28]
    input_list = [1, 5, 2, 4, 45, 10, 25, 28]
    assert expected_result == get_list_even(input_list)
    # Test4:
    expected_result = [2, 4, 10, 28]
    input_list = [1, 'c', 5, 2, 4, 'a', 45, 10, 25, 28]
    assert expected_result == get_list_even(input_list)
