# Write a program to count the occurrences of a specific character in a string.

# Steps:
# 1. Iterate the string to evaluate each character in the string till end of string.
# 2. Create a dictionary, with the char -> count
# 3. Check if the char exists in the dictionary increment the count or just add a new key with count = 1

# Tests:
# 1. Check with alphanumerics string without spaces.
# 2. Check with alphanumeric string with spaces.
# 3. Check with only characters ( special symbols).
# 4. Check for empty/none string

def count_characters(string_to_process):
    char_to_count = {}
    if string_to_process:
        for index in range(len(string_to_process)):
            if not string_to_process[index].isspace():
                if string_to_process[index] in char_to_count:
                    char_to_count[string_to_process[index]] = char_to_count.get(string_to_process[index])+1
                else:
                    char_to_count[string_to_process[index]] = 1
    else:
        print("Input String is empty")
    return char_to_count


if __name__ == '__main__':
    counts = count_characters(input("Enter the input string : "))
    print(f'Counts of characters in the string are : {counts}')

    new_string = input('Enter the new input string : ')
    input_symbol = input('Enter the character to be counted : ')
    print(f'Count for the character {input_symbol} in the string {new_string}  : {new_string.count(input_symbol)}')



