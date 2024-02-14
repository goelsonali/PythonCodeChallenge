# Test class for challenge Day35.
# Write a simple unit test for a function that adds two numbers.

from challenges.Day35 import add_numbers


# Test Cases
# 1. Check if data type is float for 1 argument.
# 2. Check if data type is int for 1 argument.
# 3. Check if data type is string for 1 argument.
# 4. Check for both valid int and float arguments.
# 5. Check for both argument with string type.


def test_add_numbers():
    # Test 1 and 2:
    expected_result = 6.1
    test_num1 = 4.1
    test_num2 = 2
    assert expected_result == add_numbers(test_num1, test_num2)
    assert expected_result == add_numbers(test_num2, test_num1)
    # Test 3:
    expected_result = 6.0
    test_num1 = 4.0
    test_num2 = "2"
    assert expected_result == add_numbers(test_num1, test_num2)
    assert expected_result == add_numbers(test_num2, test_num1)
    # Test 4:
    expected_result = 7
    test_num1 = 4
    test_num2 = 3
    assert expected_result == add_numbers(test_num1, test_num2)
    expected_result = 7.0
    test_num1 = 4.0
    test_num2 = 3.0
    assert expected_result == add_numbers(test_num2, test_num1)
    # Test 5:
    expected_result = 8.0
    test_num1 = "4"
    test_num2 = "4"
    assert expected_result == add_numbers(test_num1, test_num2)
    test_num1 = "4.0"
    test_num2 = "4.0"
    assert expected_result == add_numbers(test_num1, test_num2)