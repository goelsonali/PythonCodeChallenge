# Create a program to calculate the area of a circle given its radius.

def evaluate_area_circle(r):
    return 3.14 * r ** 2


radius = int(input("Enter radius of a circle : "))
print(f'Area of a circle with radius  {radius} is : ' + str(evaluate_area_circle(radius)))

# Write a Python program to calculate the difference between a given number and 17.
# If the number is greater than 17, return twice the absolute difference.


def evaluate(num):
    if num > 17:
        return abs(num-17)*2
    else:
        return abs(17-num)


print(f'The result of the evaluation is : {evaluate(int(input("Enter the number for evaluation : ")))}')


# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

print(str(int(input("Enter no of copies : ")) * input("For this string")))
