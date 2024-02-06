# Create a program that uses a lambda function to square each element of a list.


# Test Cases :
# 1. Check if the list is empty.
# 2. Check if returned list has each element is a square.


def perform_list_evaluation(input_list_to_process):
    if input_list_to_process:
        return list(map(lambda x: x * x, input_list_to_process))
    else:
        return 'Input list is empty'


if __name__ == '__main__':
    in_list = [2, 4, 6]
    print(f'Input list is - {in_list} and the transformed list is - {perform_list_evaluation(in_list)}')
