from random import *
from eval import calc
def generate_quiz():
    #viết hàm generate_quiz để trả ra x, y, op, result random
    # Hint: Return [x, y, op, result]
    ops = ['+', '-', '*', '/']
    x = randint(1, 10)
    y = randint(1, 10)
    op = choice(ops)
    err = randint(-1, 1)

    res = calc(x, y, op) + err
    return [x, y, op, res]

def check_answer(x, y, op, result, user_choice):
#dựa vào x, y, op, result, user_choice ===> True or False
    if user_choice == True and result == calc(x, y, op):
        return True
    elif user_choice == False and result != calc(x, y, op):
        return True
    else:
        return False
