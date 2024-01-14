# Tests for Day5 challenge
from challenges.Day5 import get_max_min


# Test Cases:
# a. Check for all int elements
# b. Check for all float elements
# c. Check for mixed int,float and String elements
# d. Check for only string elements

def test_all_int():
    list_to_test = [1, 2, 38, 10]
    assert get_max_min(list_to_test) == (38, 1)


def test_all_float():
    list_to_test = [1.8, 2.4, 3.4, 10.07, 5.0]
    assert get_max_min(list_to_test) == (10.07, 1.8)


def test_all_mixed():
    list_to_test = [1.8, 2.4, 3, 10, 'test', 'string']
    assert get_max_min(list_to_test) == (10, 1.8)


def test_all_strings():
    list_to_test = ['test', 'string']
    assert get_max_min(list_to_test) == (0, 0)