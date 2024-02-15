# Write a Python program to check if two strings are anagrams.
import collections


# Anagram means - An anagram of a string is another string that contains the same characters, only the order of characters can be different.

def check_for_anagram_strings(input_str1, input_str2):
    is_anagram = False
    if input_str1 and input_str2:
        if len(input_str1) == len(input_str2):
            list_of_char_str1 = list(map(lambda s: s, input_str1))
            list_of_char_str2 = list(map(lambda s: s, input_str2))
            if collections.Counter(list_of_char_str1) == collections.Counter(list_of_char_str2):
                is_anagram = True
    else:
        return 'The provided input is empty'
    return is_anagram


print(check_for_anagram_strings('abce', 'dabc'))