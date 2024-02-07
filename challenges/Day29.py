# Create a function that generates a random number between a given range.
from random import uniform, randint


def random_number_using_uniform(from_range, to_range):
    if from_range != to_range and from_range < to_range:
        return uniform(from_range, to_range)
    else:
        return 'The range provided is incorrect'


def random_number_using_randint(from_range, to_range):
    if from_range != to_range and from_range < to_range:
        return randint(from_range, to_range)
    else:
        return 'The range provided is incorrect'


if __name__ == '__main__':
    print(f'Generate random number using uniform function returns float : {random_number_using_uniform(1, 5)}')
    print(f'Generate random number using randint function returns int : {random_number_using_randint(1, 5)}')
