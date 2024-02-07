# Write a program to remove vowels from a given string.


def remove_vowels(input_to_process):
    if input_to_process:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        new_str = ''
        for index in range(len(input_to_process)):
            if input_to_process[index].lower() not in vowels:
                new_str += input_to_process[index]
        return new_str
    else:
        return 'String is empty'


if __name__ == '__main__':
    print(f'{remove_vowels("I am in the world of python For You")}')