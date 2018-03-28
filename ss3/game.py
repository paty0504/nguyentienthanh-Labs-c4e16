from random import randint, choice
from eval import calc
import random
ops = ['+', '-']

x = randint(1, 10)
y = randint(1, 10)
op = choice(ops)
error = choice([-1, 0, 1])
res = calc(x, y, op)
r = res + error
# if op == '+':
#     result = x + y + error
# elif op == '-':
#     result = x - y + error
# elif op == '*':
#     result = x * y + error
# elif op == '/':
#     result = x/y + error
print('{0} {1} {2} = {3} '.format(x, op, y, r))
ans = input('Y/N: ').lower()
if error == 0:
    if ans == 'y':
        print('Yay')
    elif ans == 'n':
        print('Wrong')
elif error != 0:
    if ans == 'y':
        print('Wrong')
    elif ans == 'n':
        print('Yay')
