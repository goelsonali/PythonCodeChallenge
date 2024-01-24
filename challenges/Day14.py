# Write a program to print the first n numbers of a Fibonacci sequence

# Test cases:
# 1. Check with non-int type input.
# 2. Check with input as 1.
# 3. Check with input with some valid range.


def fibonacci_seq(input_number):
    if input_number <= 0:
        return 0
    elif input_number == 1:
        return 1
    else:
        return fibonacci_seq(input_number - 1) + fibonacci_seq(input_number - 2)


def print_fibonacci_seq(input_number):
    if isinstance(input_number, int):
        fib_sequence = []
        for i in range(0, input_number):
            fib_sequence.append(fibonacci_seq(i))
        return fib_sequence
    else:
        return 'Incorrect type of input'


if __name__ == '__main__':
    series = int(input("Enter the range of the fibonacci series : "))
    print(f'The series is : {print_fibonacci_seq(series)}')


# Sample Output
# Enter the range of the fibonacci series : 5
# The series is : [0, 1, 1, 2, 3]
