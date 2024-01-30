# Create a program to remove a specific element from a set.

# Test Cases:
# 1. Check for mixed type values.
# 2. Check for same type values.
# 3. Check for empty set.


def remove_element(input_set, element_to_remove):
    if input_set:
        input_set = set(x for x in input_set if x != element_to_remove)
        return input_set
    else:
        return 'The input set is empty'


if __name__ == '__main__':
    in_set = {'abc', '1', '2', 45}
    element_to_remove = 45
    print(f' After removing the element - {element_to_remove} from set - {in_set}\n result is : {remove_element(in_set, element_to_remove)}')


# Sample Output :
# After removing the element - 45 from set - {'2', 'abc', 45, '1'}
# result is : {'2', 'abc', '1'}