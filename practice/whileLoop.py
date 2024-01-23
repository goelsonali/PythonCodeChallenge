# Write a program for below scenario :
# Input any non-negative and non-zero integer number and name it c0;
# 1.if it's even, evaluate a new c0 as c0 ÷ 2;
# 2. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# 3. if c0 ≠ 1, skip to point 2.

c0 = int(input("enter number -"))
counter = 0
while c0 > 1:
    counter += 1
    if c0 % 2 == 0:
        c0 = c0//2
    elif c0 % 2 == 1:
        c0 = 3*c0+1
    elif c0 != 1:
        continue
    else:
        break
    print(c0)

print(f'steps = {counter}')