# Tests for the challenge Day22 -
# Create a program to find the second-largest element in a list.

from challenges.Day22 import find_second_largest


# Test Cases:
# 1. Check for a list with only int type.
# 2. Check for a list with only float type.
# 3. Check for a list with mixed int and float type.
# 4. Check for an empty list.


def test_find_second_largest():
    # TestCase 1:
    expected_result = 35
    in_list = [1, 2, 50, 35, 6]
    assert expected_result == find_second_largest(in_list)
    # TestCase 2:
    expected_result = 20.5
    in_list = [1.0, 2.5, 20.1, 20.5, 26.1]
    assert expected_result == find_second_largest(in_list)
    # TestCase 3:
    expected_result = 26
    in_list = [1, 2.5, 20.1, 20.5, 26, 34]
    assert expected_result == find_second_largest(in_list)
    # TestCase 4:
    expected_result = 'Input list is empty'
    in_list = []
    assert expected_result == find_second_largest(in_list)