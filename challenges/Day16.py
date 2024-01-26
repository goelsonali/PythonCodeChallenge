# Write a function that counts the frequency of each word in a sentence.


# Test Cases :
# 1. Check for uppercase and lowercase words.
# 2. Check for only uppercase words and digits.
# 3. Check for input if not string return error message.
# 4. Check for empty string.
# 5. Check for additional spaces.


def count_words(input_sentence):
    result = ''
    try:
        if input_sentence:
            split_list = input_sentence.split()
            word_dic = {}
            for w in split_list:
                if word_dic.get(w):
                    word_dic[w] = word_dic.get(w) + 1
                else:
                    word_dic[w] = 1
            result = word_dic
        else:
            result = 'Input is an empty string'
    except AttributeError:
        print('Invalid type of input')

    return result


if __name__ == '__main__':
    print(count_words('I am in a world of python !!, and in a world of joy'))
    print(count_words(''))
    print(count_words(int(input('Enter a sentence :'))))

# Sample output
# {'I': 1, 'am': 1, 'in': 2, 'a': 2, 'world': 2, 'of': 2, 'python': 1, '!!,': 1, 'and': 1, 'joy': 1}
# Input is an empty string
# Enter a sentence :123
# Invalid type of input
