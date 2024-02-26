# Write a program to flatten a nested list.

# Steps:
# a. Assume the nested list is a 3-dimensional list [ [1,2], [3,4], [5,6]]
# b. Declare an empty "result_list" and Iterate the original list.
# c. Perform another forloop for the inner list and add the element of that list to the "result_list"

def with_for_loop_flatten_list(nested_list):
    result_list = []
    if nested_list:
        for index in range(len(nested_list)):
            for element in range(len(nested_list[index])):
                result_list.append(nested_list[index][element])
    return result_list


def with_comprehension_flatten_list(nested_list):
    if nested_list:
        # Comprehension syntax - [(expression(item) for item in iterable]
        return [element for row in nested_list for element in row]


if __name__ == '__main__':
    input_list = [[1, 2], [3, 4], [5, 6]]
    print(f' Evaluate nested list {input_list} using for loop, result -  {with_for_loop_flatten_list(input_list)}')
    print(f' Evaluate nested list {input_list} using comprehension, result -  {with_comprehension_flatten_list(input_list)}')

