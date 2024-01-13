from challenges.Day3 import count_vowels


# a. Check for empty string
def test_empty_string():
    assert count_vowels("") == 'Empty String provided'


# b.Check with all Uppercase letters
def test_with_all_uppercase():
    assert count_vowels("I AM VERY HAPPY") == 4


# b.Check with all lowercase letters
def test_with_all_lowercase():
    assert count_vowels("i am very happy") == 4


# b.Check with mixedcase  letters
def test_with_all_lowercase():
    assert count_vowels("I am Very hAppy") == 4