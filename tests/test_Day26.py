# Test class for the Day26 challenge
# Create a program that uses a lambda function to square each element of a list.

from challenges.Day26 import perform_list_evaluation

# Test Cases :
# 1. Check if the list is empty.
# 2. Check if returned list has each element is a square.


def test_check_list():
    # TestCase 1:
    expected_result = 'Input list is empty'
    in_list = []
    assert expected_result == perform_list_evaluation(in_list)
    # TestCase 2:
    expected_result = [1, 4, 9]
    in_list = [1, 2, 3]
    assert expected_result == perform_list_evaluation(in_list)