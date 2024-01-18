# This is the test class for the challenge Day8

from challenges.Day8 import evaluate_case_n_count

# Tests:
# 1. Check for empty string.
# 2. Check if string contains alphanumeric with spaces.


def test_for_upper_lower():
    test_input_string = 'I am very Happy. So lets $$'
    expected_count = {'uppercase' : 3, 'lowercase' : 15}
    expected_default_count = {'uppercase': 0, 'lowercase': 0}
    assert expected_default_count == evaluate_case_n_count("")  # Test for the empty string
    assert expected_count == evaluate_case_n_count(test_input_string)