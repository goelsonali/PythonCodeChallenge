# Write a program to remove duplicate from a list


# Test Cases :
# 1. Check for string type list.
# 2. Check for float and int type list.
# 3. Check for empty list.


def remove_duplicates(input_list):
    if input_list:
        result_set = set(x for x in input_list)
        return result_set
    else:
        return 'Empty list'


if __name__ == '__main__':
    in_list = ['a', 'A', 'b', 'a', 'b']
    print(f'Input list {in_list}')
    print(f'Resulted list  {remove_duplicates(in_list)}')

    in_list = [1, 2, 3, 5, 2, 3.0, 2.0, 1]
    print(f'Input list {in_list}')
    print(f'Resulted list  {remove_duplicates(in_list)}')

    in_list = []
    print(f'Resulted list  {remove_duplicates(in_list)}')