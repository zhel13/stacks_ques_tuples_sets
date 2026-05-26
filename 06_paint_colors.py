from collections import deque

def check_color(c, arr):

    if c == 'purple' and 'blue' in arr and 'red' in arr:
        return True
    elif c == 'orange' and 'red' in arr and 'yellow' in arr:
        return True
    elif c == 'green' and 'blue' in arr and 'yellow' in arr:
        return True
    elif c == 'yellow' or color == 'blue' or color == 'red':
        return True
    else:
        return False

colors = deque(input().split())
main_colors = ['red', 'yellow', 'blue', 'purple', 'orange', 'green']


formed_colors = []
result = ''

# secondary colors:
# orange = red + yellow
# purple = red + blue
# green = yellow + blue

while colors:
    first_string = colors.popleft()
    second_string = colors.pop() if colors else ''

    for color in (first_string + second_string, second_string + first_string):
        if color in main_colors:
            formed_colors.append(color)
            break
    else:
        if len(first_string) > 1:
            colors.insert(len(colors) // 2, first_string[:-1])
        if len(second_string) > 1:
            colors.insert(len(colors) // 2, second_string[:-1])

for color in formed_colors:
    if not check_color(color, formed_colors):
        formed_colors.remove(color)

print(formed_colors)

