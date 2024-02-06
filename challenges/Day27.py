# Create a program that sorts a list of strings alphabetically.

# Test Cases :
# 1. Check if the string is empty.
# 2. Check if the list is mixed case.
# 4. Check if the list is lower case.

def sort_list_alphabetically(input_list_of_strings):
    if input_list_of_strings:
        return sorted(input_list_of_strings, key= str.lower)
    else:
        return 'The list is empty'


if __name__ == '__main__':
    in_list_of_string = ['d', 'abc', 'b', 'cde', 'e', 'a']
    print(f' The input list of string is : {in_list_of_string} the sorted list alphabetically is {sort_list_alphabetically(in_list_of_string)}')
    in_list_of_string = ['D', 'abc', 'Bcg', 'cde', 'F', 'a', 'b']
    print(f' The input list of string is : {in_list_of_string} the sorted list alphabetically is {sort_list_alphabetically(in_list_of_string)}')