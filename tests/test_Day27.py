# Test class for the Day27 challenge
# Create a program that sorts a list of strings alphabetically.

from challenges.Day27 import sort_list_alphabetically

# Test Cases :
# 1. Check if the list is empty.
# 2. Check if the list is mixed case.
# 4. Check if the list is lower case.


def test_check_list():
    # TestCase 1:
    expected_result = 'The list is empty'
    in_list = []
    assert expected_result == sort_list_alphabetically(in_list)

    # TestCase 2:
    expected_result = ['a', 'be', 'I', 'python', 'The']
    in_list = ['a', 'I', 'The', 'python', 'be']
    assert expected_result == sort_list_alphabetically(in_list)

    # TestCase 3:
    expected_result = ['i', 'learn', 'python', 'to', 'want']
    in_list = ['i', 'want', 'to', 'learn', 'python']
    assert expected_result == sort_list_alphabetically(in_list)


