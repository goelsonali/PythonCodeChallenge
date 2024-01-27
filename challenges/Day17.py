# Create a program that capitalizes the first letter of each word in a sentence.


# Test Cases :
# 1. Check for sentence already starting with first capital letter.
# 2. Check for sentence with first letter as lowercase.
# 3. Check for empty not sentence.
# 4. Check for first word with first letter multiple times.


def capital_first_letter_ootb(sentence):
    if sentence:
        result = sentence.capitalize()
    else:
        result = 'The sentence is empty'
    return result


def capital_first_letter_custom(sentence):
    if sentence:
        first_word = sentence.split()[0]
        letters = []
        for l in range(len(first_word)):
            if l == 0:
                letters.append(first_word[l].upper())
            else:
                letters.append(first_word[l])
        result = sentence.replace(first_word, ''.join(letters))
    else:
        result = 'The sentence is empty'
    return result


if __name__ == '__main__':
    print(capital_first_letter_ootb('it is in python ootb function '))
    print(capital_first_letter_ootb('It is in python ootb function'))
    print(capital_first_letter_custom('test in python custom function'))

# Sample output
# It is in python ootb function
# It is in python ootb function
# Test it is in python custom function
