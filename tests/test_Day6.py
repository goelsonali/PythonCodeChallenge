# Test class for the Day6 challenge

from challenges.Day6 import count_characters


# Tests:
# 1. Check with alphanumerics string without spaces.
# 2. Check with alphanumeric string with spaces.
# 3. Check with only characters ( special symbols).
# 4. Check for empty/none string

def test_alpha_without_n_with_space():
    input_string_without_space = 'abbcc123acd1'
    input_string_with_space = 'abbcc 123 ac d1'
    input_string_with_symbols = '£@ 123 £ d1'
    expected_dic_alpha_numeric = {
        'a': 2,
        'b': 2,
        'c': 3,
        '1': 2,
        '2': 1,
        '3': 1,
        'd': 1
    }
    expected_dic_symbols = {
        '£': 2,
        '@': 1,
        '1': 2,
        '2': 1,
        '3': 1,
        'd': 1
    }
    assert count_characters(input_string_without_space) == expected_dic_alpha_numeric
    assert count_characters(input_string_with_space) == expected_dic_alpha_numeric
    assert count_characters(input_string_with_symbols) == expected_dic_symbols
