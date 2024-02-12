# Write a test case for a function that checks if a number is prime

def prime_number_func(num):
    if num == 0 or num == 1:
        return 'The number is neither prime not composite'
    elif num == 2:
        return 'Prime number'
    else:
        flag = True
        if num == 4:
            flag = False
        for x in range(2, num//2 ):
            if num % x == 0:
                flag = False
                break
        if flag:
            return 'Prime number'
        else:
            return 'Not Prime number'


print(prime_number_func(6))