# Create a program that checks if a given string is a valid email address.

# Test cases
# 1. Check for empty string if empty return specific message.
# 2. Check for valid email with characters in the string - '@' and '.com' only once.
# 3. Check for invalid email with characters in the string - '@' more than once.
# 4. Check for invalid email with characters in the string - '@' and '.com' only once but has space.
# 5. Check for invalid email with missing characters in the string - '@' or '.com' or both.


def check_for_valid_email(email_address):
    if email_address:
        is_valid = False
        if email_address.count('@') == 1 and email_address.count('.com') == 1 and email_address.count(' ') == 0:
            is_valid = True
        return is_valid
    else:
        return 'The input email address is empty'


if __name__ == '__main__':
    print(f' The check for the input email address if valid :  {check_for_valid_email(input("Enter an email address"))}')
