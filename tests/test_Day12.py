# Tests for the challenge Day12 -
# Write a program to reverse a given string.

from challenges.Day12 import reverse_string


# Tests Cases:
# 1. Test for an empty string.
# 2. Test string with spaces.
# 3. Test string with no spaces.


def test_reversed_string():
    # Test case 1
    assert 'It is an empty string' == reverse_string('')

    # Test case 2
    expected_result = 'now happy'
    assert expected_result == reverse_string('happy now')

    # Test case 1
    expected_result = 'python'
    assert expected_result == reverse_string('python')

