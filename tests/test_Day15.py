# Tests for the challenge Day15 -
# Create a program that checks if a year is a leap year.

from challenges.Day15 import check_for_leap


# Test Cases :
# 1. Check for the valid date format.
# 2. Check for a non-leap year.
# 3. Check for a leap year.


def test_for_leap_year():
    #Test case : 1
    expected_result = 'Enter the date in a valid format : yyyy-mm-dd'
    assert expected_result == check_for_leap('2019/01/10')
    # Test case : 2
    expected_result = 'It is not a leap year'
    assert expected_result == check_for_leap('2023-01-10')
    # Test case : 3
    expected_result = 'It is a leap year'
    assert expected_result == check_for_leap('2024-01-10')