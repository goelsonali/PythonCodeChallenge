# Tests for the challenge Day18 -
# Write a function to calculate the factorial of a number.
import pytest

from challenges.Day19 import find_factorial


# Test Cases:
# 1. Check the type only int type is accepted.
# 2. Check for input number 0.
# 3. Check for any number > 1.


def test_find_factorial():
    # Test1 :
    expected_exception = 'The input type can be a whole number only.'
    input_record = 'abc'
    with pytest.raises(Exception) as e:
        find_factorial(input_record)
        assert expected_exception in str(e.value)
        assert e.type == ValueError
    # Test2 :
    expected_result = 'Number should be greater than Zero.'
    input_record = 0
    assert expected_result == find_factorial(input_record)
    # Test3 :
    expected_result = 120
    input_record = 5
    assert expected_result == find_factorial(input_record)
