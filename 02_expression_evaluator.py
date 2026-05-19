from functools import reduce

possible_operators = ['*', '+', '-', '/']


string_expression = input().split()
result = 0
initial = []
operator = ''

while string_expression:
    if string_expression[0].lstrip('+-').isdigit():
        initial.append(int(string_expression.pop(0)))
    else:
        operator = string_expression.pop(0)
        if operator == "*":
            result = reduce(lambda x, y: x * y, initial)
        elif operator == "+":
            result = reduce(lambda x, y: x + y, initial)
        elif operator == "-":
            result = reduce(lambda x, y: x - y, initial)
        elif operator == "/":
            result = reduce(lambda x, y: x // y, initial)

        initial.clear()
        initial.append(result)
print(*initial)
