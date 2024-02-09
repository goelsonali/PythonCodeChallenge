# Test class for Day31 challenge
# Create a program that checks if a given string is a valid email address.

from challenges.Day31 import check_for_valid_email


# Test cases
# 1. Check for empty string if empty return specific message.
# 2. Check for valid email with characters in the string - '@' and '.com' only once.
# 3. Check for invalid email with characters in the string - '@' more than once.
# 4. Check for invalid email with characters in the string - '@' and '.com' only once but has space.
# 5. Check for invalid email with missing characters in the string - '@' or '.com' or both.


def test_valid_email():
    # Test 1:
    expected_result = 'The input email address is empty'
    assert expected_result == check_for_valid_email('')
    # Test 2:
    expected_result = True
    test_email = 'ilearn@python.com'
    assert expected_result == check_for_valid_email(test_email)
    # Test 3:
    expected_result = False
    test_email = 'i@learn@python.com'
    assert expected_result == check_for_valid_email(test_email)
    # Test 4:
    expected_result = False
    test_email = 'i learn @python.com'
    assert expected_result == check_for_valid_email(test_email)
    # Test 5:
    # Missing @
    expected_result = False
    test_email = 'ipython.com'
    assert expected_result == check_for_valid_email(test_email)
    # Missing .com
    expected_result = False
    test_email = 'i@python'
    assert expected_result == check_for_valid_email(test_email)
    # Missing @ and .com
    expected_result = False
    test_email = 'i@python'
    assert expected_result == check_for_valid_email(test_email)
