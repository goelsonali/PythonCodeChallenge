# Tests for the challenge Day11 -
# Write a program to print the multiplication table of a given number.

from challenges.Day11 import print_multiplication_table
# Test cases:
# 1. Check for O and 1 as input number.
# 2. Check for any string/float type.
# 3. Check for any number.


def test_multiplication_table():
    # Test case 1
    expected_result = 'Enter number greater than 1'
    assert expected_result == print_multiplication_table(1)

    # Test case 2
    expected_result = 'Incorrect input type'
    assert expected_result == print_multiplication_table('123')

    # Test case 3
    #tbd