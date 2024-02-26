# Write a program that removes all whitespaces from a given string.


def remove_whitespaces(input_str):
    if input_str:
        return ''.join(s for s in input_str if not s.isspace())


print(remove_whitespaces("I am now learning python"))