# Write a function to count the number of vowels in a given string
import string


# Steps :
# 1. Take the input strng and store in a variable.
# 2. Then evaluate each character of the string using a loop from 0 to length of the string.
# 3. Checks if the character is either a vowel or not , if yes increment the count.
# 4. Print the count.

# Tests :
# a. Check for empty string
# b. Check with all Uppercase letters
# c. Check with all lowercase letters
# d. Check with mixed case letters
def count_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    if len(input_string) > 0:
        for index in range(0, len(input_string)):
            if input_string[index].lower() in vowels:
                count += 1
        return count
    else:
        return "Empty String provided"


# Function invocation
input_user = input('Enter any string to count the vowels :')
print(f'The no. of vowels in the provided string are : {count_vowels(input_user)}')


