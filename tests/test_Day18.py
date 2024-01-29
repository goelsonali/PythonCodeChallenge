# Tests for the challenge Day18 -
# Create a program to find the largest among three numbers.
import pytest

from challenges.Day18 import max_number


# Test Cases
# 1. Check if the type of input is int if not throw an error.
# 2. Check with input as str type.
# 3. Check with input as int type.
# 4. Check if input is empty.


def test_max_number():
    # Test1 :
    expected_exception = 'The input is not a number'
    input_numbers = ['45','ab','10']
    with pytest.raises(Exception) as e:
        max_number(input_numbers)
        assert expected_exception in str(e.value)
        assert e.type == ValueError
    # Test2 :
    expected_result = 45
    input_numbers = ['45', '20', '10']
    assert expected_result == max_number(input_numbers)
    # Test3 :
    expected_result = 45
    input_numbers = [45, 20, 10]
    assert expected_result == max_number(input_numbers)
    # Test4 :
    expected_result = 'No input'
    input_numbers = []
    assert expected_result == max_number(input_numbers)