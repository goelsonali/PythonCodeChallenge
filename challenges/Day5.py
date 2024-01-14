# Write a program to find the maximum and minimum values in a list.

# Steps:
# 1. Iterate the list and check for the type of each element ( int or float )
# 2. If not ( int or float ) throw an exception "Invalid element type"
# 3. Find the max element and the min element in the list

# Test Cases:
# a. Check for all int elements
# b. Check for all float elements
# c. Check for mixed int,float and String elements
# d. Check for only string elements

def evaluate_list(list_to_process):
    refined_list = []
    error_list = []
    for i in range(len(list_to_process)):
        if isinstance(list_to_process[i], int) or isinstance(list_to_process[i], float):
            refined_list.append(list_to_process[i])
        else:
            error_list.append(list_to_process[i])
    return refined_list, error_list


def get_max_min(processing_list):
    correct_list, error_list = evaluate_list(processing_list)
    if error_list:
        print(f'The list contains invalid elements : ', *error_list, sep=',')
        max_number, min_number = (0, 0)
    if correct_list:
        correct_list.sort()
        max_number, min_number = max(correct_list), min(correct_list)
    return max_number, min_number


if __name__ == "__main__":
    input_list = [1.9, 2, 3.10, 5.3, 'we', 'for', 34]
    if input_list:
        max_num, min_num = get_max_min(input_list)
        print(f'Maximum number in the list : {max_num} \nMinimum number in the list : {min_num}')
    else:
        print('Empty list')
