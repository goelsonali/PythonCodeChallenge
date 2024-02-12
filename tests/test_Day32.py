# Test class for Day32 challenge
# Create a program that checks if a given string is a valid email address.

from challenges.Day32 import calc_average_using_reduce, calc_average_using_sum


# Test Cases:
# 1. Check for the empty list
# 2. Check for the correct average value.


def test_calc_average():
    # Test 1:
    expected_result = 'The list is empty'
    assert expected_result == calc_average_using_reduce([])
    assert expected_result == calc_average_using_sum([])

    # Test 2:
    expected_result = 3.0
    input_test_list = [1, 2, 3, 4, 5]
    assert expected_result == calc_average_using_reduce(input_test_list)
    assert expected_result == calc_average_using_sum(input_test_list)
    assert calc_average_using_reduce(input_test_list) == calc_average_using_sum(input_test_list)