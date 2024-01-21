# Tests for the Day10 challenge

from challenges.Day10 import remove_duplicates


# Test Cases :
# 1. Check for string type list.
# 2. Check for float and int type list.
# 3. Check for empty list.


def test_remove_duplicates():
    test_string_list = ['a', 'A', 'b', 'a', 'b']
    test_mixed_int_float = [1, 2, 3, 5, 2, 3.0, 2.0, 1]

    expected_result_set_string = {'A', 'b', 'a'}
    expected_result_set_mixed = {1, 2, 3, 5}

    assert expected_result_set_string == remove_duplicates(test_string_list)
    assert expected_result_set_mixed == remove_duplicates(test_mixed_int_float)
    assert 'Empty list' == remove_duplicates([])