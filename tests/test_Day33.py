# Test class for Day32 challenge
# Write a test case for a function that checks if a number is prime

from challenges.Day33 import prime_number_func

# Test Cases :
# 1. Check for number 0 and 1, it should be not prime not composite.
# 2. Check for number 2, it should be prime.
# 3. Check for any odd number which is prime , 3-7.
# 4. Check for any odd number which is not prime , 9.
# 5. Check for any even number which is not prime, 4,6,8.


def test_prime_number_func():
    # Test 1
    expected_result = 'The number is neither prime not composite'
    assert prime_number_func(0) == expected_result
    assert prime_number_func(1) == expected_result

    # Test2
    expected_result = 'Prime number'
    assert prime_number_func(2) == expected_result

    # Test3
    expected_result = 'Prime number'
    assert prime_number_func(3) == expected_result
    assert prime_number_func(7) == expected_result

    # Test4
    expected_result = 'Not Prime number'
    assert prime_number_func(9) == expected_result

    # Test5
    expected_result = 'Not Prime number'
    assert prime_number_func(4) == expected_result
    assert prime_number_func(8) == expected_result
