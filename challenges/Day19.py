# Write a function to calculate the factorial of a number.

# Test Cases:
# 1. Check the type only int type is accepted.
# 2. Check for input number 0.
# 3. Check for any number > 1.


def find_factorial(num):
    try:
        num = int(num)
        if num > 0:
            factorial = 1
            while num > 0:
                factorial = factorial * num
                num = num - 1
            return factorial
        else:
            return 'Number should be greater than Zero.'
    except ValueError:
        print('The input type can be a whole number only.')
        return -1


if __name__ == '__main__':
    print(f'Factorial of number 5 is : {find_factorial(5)}')
    print(f'Factorial of number 10 is : {find_factorial(6)}')


# Sample Output
# Factorial of number 5 is : 120
# Factorial of number 10 is : 720