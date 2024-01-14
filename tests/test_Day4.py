# Tests for the Day4 challenege

from challenges.Day4 import sum_all_elements

# Tests:
# a. Check for all the int elements
# b. Check for all the float elements
# c. Check for mixed int and float elements
# d. Check for mixed string,float,int elements


def test_all_int():
    int_only_list = [2, 4, 6, 8]
    expected_result = 20
    assert sum_all_elements(int_only_list) == expected_result


def test_all_float():
    float_only_list = [2.1, 4.2, 6.1, 8.1]
    expected_result = 20.5
    assert sum_all_elements(float_only_list) == expected_result


def test_int_float_mixed():
    float_only_list = [2.1, 4.2, 6, 8]
    expected_result = 20.3
    assert sum_all_elements(float_only_list) == expected_result

    
def test_all_mixed():
    float_only_list = [2.1, 4.2, 6, 8, "1", "34"]
    expected_result = 20.3
    assert sum_all_elements(float_only_list) == expected_result