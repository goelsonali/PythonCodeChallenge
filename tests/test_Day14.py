# Tests for the challenge Day14 -
# Write a program to print the first n numbers of a Fibonacci sequence.

from challenges.Day14 import print_fibonacci_seq


# Test cases:
# 1. Check with non-int type input.
# 2. Check with input as 1.
# 3. Check with input with some valid range.


def test_fibonacci_series():
    # Test case 1
    assert 'Incorrect type of input' == print_fibonacci_seq('5')

    # Test case 2
    expected_result = [0]
    assert expected_result == print_fibonacci_seq(1)

    # Test case 1
    expected_result = [0, 1, 1, 2, 3, 5, 8]
    assert expected_result == print_fibonacci_seq(7)