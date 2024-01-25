# Create a program that checks if a year is a leap year.

# Test Cases :
# 1. Check for the valid date format.
# 2. Check for a non-leap year.
# 3. Check for a leap year.


def check_for_leap(input_date):
    if input_date.count('-') == 2:
        year = int(input_date.split('-')[0])
        if year % 4 == 0 or year % 400 == 0:
            result = 'It is a leap year'
        else:
            result = 'It is not a leap year'
    else:
        result = 'Enter the date in a valid format : yyyy-mm-dd'

    return result


if __name__ == '__main__':
    in_date = input('Enter a date to check if leap year or not :')
    print(check_for_leap(in_date))
