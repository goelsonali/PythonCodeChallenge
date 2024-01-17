# Write a program to check if a number is positive, negative, or zero.

# Steps:
# 1. Check for if num is 0 or not.
# 2. Check if num < 0 and check for if num >0


# Tests:
# 1. Test only positive int & float number.
# 2. Test only negative int & float number.
# 3. Test for 0.


def evaluate_number(number):
    result = 'Zero'
    if number != 0:
        if number >= 0:
            result = 'Positive'
        else:
            result = 'Negative'
    return result


if __name__ == '__main__':
    print(evaluate_number(float(input('Enter the number to be checked : '))))


# Sample output :
# Enter the number to be checked : 23.0
# Positive

