# Tests for the challenge Day16 -
# Write a function that counts the frequency of each word in a sentence.
import pytest

from challenges.Day16 import count_words


# Test Cases :
# 1. Check for uppercase and lowercase words.
# 2. Check for only uppercase words and digits.
# 3. Check for input if not string return error message.
# 4. Check for empty string.


def test_count_word():
    # Test1 :
    expected_result = {'I': 1, 'am': 1, 'in': 2, 'PYTHON': 1, 'are': 1, 'you': 1, 'it': 1, '?': 1}
    assert expected_result == count_words('I am in PYTHON are you in it ?')
    # Test2 :
    expected_result = {'I': 1, 'AM': 1, 'IN': 2, 'PYTHON': 1, 'THIS': 1, 'WORLD': 1, '3': 1}
    assert expected_result == count_words('I AM IN PYTHON 3 IN THIS WORLD')
    # Test3 :
    expected_exception = 'Invalid type of input'
    with pytest.raises(Exception) as e:
        count_words(int('123'))
        assert expected_exception in str(e.value)
        assert e.type == AttributeError

    # Test4 :
    expected_result = 'Input is an empty string'
    assert expected_result == count_words('')
