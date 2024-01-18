# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

# Steps:
# 1. Create a dictionary to be returned with {"uppercase" : "", "lowercase": ""}
# 2. Iterate the string evaluate each char and check if it is UPPERCASE or LOWERCASE.
# 3. And update the dictionary value against the key respectively.


# Tests:
# 1. Check for empty string.
# 2. Check if string contains alphanumeric with spaces.


def evaluate_case_n_count(input_string):
    case_by_count = {"uppercase": 0, "lowercase": 0}
    if input_string:
        for i in range(len(input_string)):
            if input_string[i].isupper():
                case_by_count["uppercase"] = case_by_count.get("uppercase") + 1
            elif input_string[i].islower():
                case_by_count["lowercase"] = case_by_count.get("lowercase") + 1
    return case_by_count


if __name__ == '__main__':
    print(f' String evaluation result : {evaluate_case_n_count(input("Enter a string : "))}')


# Sample Output
# Enter a string : asd WERT uuii 123
# String evaluation result : {'uppercase': 4, 'lowercase': 7}
