# Write a Python program to check if two strings are anagrams.

from challenges.Day36 import check_for_anagram_strings

# Test Cases
# 1. Check if 1 input string is empty.
# 2. Check if both strings are anagram.
# 3. Check if both strings are not anagram same length.
# 4. Check if both strings are not anagram different length.


def test_for_anagram():
    # Test 1 :
    expected_result = 'The provided input is empty'
    assert expected_result == check_for_anagram_strings('', 'abc')
    # Test 2 :
    expected_result = True
    assert expected_result == check_for_anagram_strings('cab', 'abc')
    # Test 3 :
    expected_result = False
    assert expected_result == check_for_anagram_strings('edf', 'abc')
    assert expected_result == check_for_anagram_strings('edfg', 'abc')