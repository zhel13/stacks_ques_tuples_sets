from functools import reduce

def calculate(op, iter):
    global result
    if op == "*":
        result = reduce(lambda x, y: x * y, iter)
    elif op == "+":
        result = reduce(lambda x, y: x + y, iter)
    elif op == "-":
        result = reduce(lambda x, y: x - y, iter)
    elif op == "/":
        result = reduce(lambda x, y: x // y, iter)


string_expression = input().split()
result = 0
initial = []
operator = ''

while string_expression:
    if string_expression[0].lstrip('+-').isdigit():
        initial.append(int(string_expression.pop(0)))
    else:
        operator = string_expression.pop(0)
        calculate(operator, initial)

        initial.clear()
        initial.append(result)
print(*initial)
