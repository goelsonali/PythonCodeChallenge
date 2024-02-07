# Test class for Day28 challenge
# Create a program that removes the nth element from a list.

from challenges.Day28 import remove_nth_record

# Test Cases :
# 1. Check if the list is empty.
# 2. Check if the nth record is valid.
# 3. Check for correct nth record removal.

def test_remove_nth_record():
    # Test1 :
    expected_result = 'The list is empty or nth index is incorrect'
    in_list = []
    assert expected_result == remove_nth_record(in_list, 0)
    # Test2 :
    expected_result = 'The list is empty or nth index is incorrect'
    in_list = []
    n = 1
    assert expected_result == remove_nth_record(in_list, n)
    # Test3 :
    expected_result = ['I', 'am', 2, 'and', 3]
    in_list = ['I', 'am', 'python', 2, 'and', 3]
    n = 2
    assert expected_result == remove_nth_record(in_list, n)
