# Create a program that swaps the values of two variables.
# Using Concepts of tuples, functions
def swap(val1, val2):
    temp = val1
    val1 = val2
    val2 = temp
    return val1, val2


def display(displayString, a, b):
    print(displayString, " a, b =", (a, b))


# Using Variables
a = 5
b = 50

display("Before Swap", a, b)
values_after_swap = swap(a, b)
display("After Swap ", values_after_swap[0], values_after_swap[1])


# Output :
# Before Swap  a, b = (5, 50)
# After Swap   a, b = (50, 5)
