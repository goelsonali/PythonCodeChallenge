# Write a program to find the sum of all elements in a list.

# Steps:
# 1. Check for the type of the element if it is int or float.
# 2. If int or float then "add" the element to the result.

# Tests:
# a. Check for all the int elements
# b. Check for all the float elements
# c. Check for mixed int and float elements
# d. Check for mixed string,float,int elements


def sum_all_elements(list_to_evaluate):
    result = 0
    for i in range(0, len(list_to_evaluate)):
        if isinstance(list_to_evaluate[i], int) or isinstance(list_to_evaluate[i], float):
            result += list_to_evaluate[i]
    return result


if __name__ == "__main__":
    input_list = [2, 4, 5, 3.5, 6.7]
    print(f'Sum of the elements are : {sum_all_elements(input_list)}')
