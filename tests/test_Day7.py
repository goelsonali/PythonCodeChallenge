# Test class for the challenge Day 7

from challenges.Day7 import evaluate_number

# Tests:
# 1. Test only positive int & float number.
# 2. Test only negative int & float number.
# 3. Test for 0.


def test_evaluate_number():
    test1_input1 = 24
    test1_input2 = 2.0
    test2_input1 = -100
    test2_input2 = -32.0
    test3_input = 0

    expected_result1 = 'Positive'
    expected_result2 = 'Negative'
    expected_result3 = 'Zero'

    assert expected_result1 == evaluate_number(test1_input1)
    assert expected_result1 == evaluate_number(test1_input2)
    assert expected_result2 == evaluate_number(test2_input1)
    assert expected_result2 == evaluate_number(test2_input2)
    assert expected_result3 == evaluate_number(test3_input)

