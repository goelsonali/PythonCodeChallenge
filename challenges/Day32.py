# Create a function that calculates the average of a list of numbers.
import operator
from functools import reduce


# Test Cases:
# 1. Check for the empty list
# 2. Check for the correct average value.
def calc_average_using_reduce(list_to_process):
    if list_to_process:
        average = reduce(operator.add, list_to_process)/len(list_to_process)
        return average
    else:
        return 'The list is empty'


def calc_average_using_sum(list_to_process):
    if list_to_process:
        average = sum(list_to_process)/len(list_to_process)
        return average
    else:
        return 'The list is empty'


if __name__ == '__main__':
    intput_list = [2, 3, 4, 5]
    print(f'The average of the list elements {intput_list} is : {calc_average_using_reduce(intput_list)} using reduce function')
    print(f'The average of the list elements {intput_list} is : {calc_average_using_sum(intput_list)} using sum function')