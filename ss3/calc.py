from operator import add, sub, mul, truediv
x = int(input('x = '))
y = int(input('y = '))
# operation = {
# "+" = add,
# "-" = sub,
# "*" = mul,
# "/" = truediv
# }
result = 0
op = input('operation(+, -, *, /)')
if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x*y
elif op == "/":
    result = x/y
print('{0} {1} {2}= {3}'.format(x, op, y, result))
