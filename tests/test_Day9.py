# This is the test class for the challenge Day8
import pytest
from challenges.Day9 import evaluate_odd_even


# Tests:
# 1. Check for if the number is greater than 0 if not print 'Invalid Number' message.
# 2. Check for the TYPE if not int throw an exception.
# 3. Check for valid number and print odd or even.

def test_evaluate_odd_even_with_exception():
    float_input = '3.0'
    with pytest.raises(Exception) as e:
        evaluate_odd_even(float_input)
        assert 'Incorrect type of number' in str(e.value)
        assert e.type == ValueError


def test_evaluate_odd_even():
    assert 'Invalid number' == evaluate_odd_even('0')
    assert 'Even' == evaluate_odd_even('24')
    assert 'Odd' == evaluate_odd_even('13')
