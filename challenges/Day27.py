# Create a program that sorts a list of strings alphabetically.

# Test Cases :
# 1. Check if the string is empty.
# 2. Check if the list is mixed case.
# 3. Check if the list is lower case.
# 4. Check if the list has only 1 string.

def sort_list_alphabetically(input_list_of_strings):
    if input_list_of_strings:
        lower_case_string = list(map(lambda s: s.lower(), input_list_of_strings))
        lower_case_string.sort()
        return lower_case_string
    else:
        return 'The list is empty'


if __name__ == '__main__':
    in_list_of_string = ['d', 'abc', 'b', 'cde', 'e', 'a']
    print(f' The input list of string is : {in_list_of_string} the sorted list alphabetically is {sort_list_alphabetically(in_list_of_string)}')