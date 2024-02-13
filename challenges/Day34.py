# Write a Python program to merge two dictionaries.


# Test Cases -
# 1. Check for dictionaries if both are empty.
# 2. Check if 1 dictionary is empty.
# 3. Check for correct merged dictionary. (Consider each dictionary is distinct)


def merge_dic(dict1, dict2):
    merged_dic = {}
    if not dict1 and not dict2:
        return 'The input dictionaries are empty'
    elif not dict2:
        merged_dic.update(dict1)
    elif not dict1:
        merged_dic.update(dict2)
    else:
        merged_dic.update(dict1)
        merged_dic.update(dict2)
    return merged_dic


if __name__ == '__main__':
    dict1 = {'a': 1, 1: 1.0}
    dict2 = {'b': 2, 2: 2.0}
    merge_dic(dict1, dict2)
    print(f' Merging the dictionary 1 - {dict1} and dictionary 2 - {dict2} \n result is : {merge_dic(dict1, dict2)}')


# Sample output:
#  Merging the dictionary 1 - {'a': 1, 1: 1.0} and dictionary 2 - {'b': 2, 2: 2.0}
#  result is : {'a': 1, 1: 1.0, 'b': 2, 2: 2.0}
