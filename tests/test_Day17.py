# Tests for the challenge Day17 -
# Create a program that capitalizes the first letter of each word in a sentence.

from challenges.Day17 import capital_first_letter_custom, capital_first_letter_ootb


# Test Cases :
# 1. Check for sentence already starting with first capital letter.
# 2. Check for sentence with first letter as lowercase.
# 3. Check for empty not sentence.
# 4. Check for first word with first letter multiple times.

def test_cap_first_letter_ootb():
    # Test case 1:
    expected_result = 'Now python with ootb function'
    assert expected_result == capital_first_letter_ootb('Now python with ootb function')
    # Test case 2:
    expected_result = 'Now python with ootb function'
    assert expected_result == capital_first_letter_ootb('now python with ootb function')
    # Test case 3:
    expected_result = 'The sentence is empty'
    assert expected_result == capital_first_letter_ootb('')
    # Test case 4:
    expected_result = 'Test python with ootb function'
    assert expected_result == capital_first_letter_ootb('test python with ootb function')


def test_cap_first_letter_custom():
    # Test case 1:
    expected_result = 'Now python with custom function'
    assert expected_result == capital_first_letter_custom('Now python with custom function')
    # Test case 2:
    expected_result = 'Now python with custom function'
    assert expected_result == capital_first_letter_custom('now python with custom function')
    # Test case 3:
    expected_result = 'The sentence is empty'
    assert expected_result == capital_first_letter_custom('')
    # Test case 4:
    expected_result = 'Test python with custom function'
    assert expected_result == capital_first_letter_custom('test python with custom function')