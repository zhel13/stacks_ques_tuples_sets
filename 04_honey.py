from collections import deque

def calculation(bee, collected_nectar, operator, honey_made):
    if operator == '+':
        honey_made.append(bee + collected_nectar)
    elif operator == '*':
        honey_made.append(bee * collected_nectar)
    elif operator == '-':
        honey_made.append(abs(bee - collected_nectar))
    elif operator == '/':
        if collected_nectar == 0:
            return
        else:
            honey_made.append(bee / collected_nectar)


working_bees = deque(int(x) for x in input().split())
nectar = [int(n) for n in input().split()]
symbols = deque(input().split())

total_honey = []

while working_bees and nectar:
    if working_bees[0] <= nectar[-1]:
        calculation(working_bees[0], nectar[-1], symbols[0], total_honey)
        working_bees.popleft()
        nectar.pop()
        symbols.popleft()
    else:
        nectar.pop()

print(f'Total honey made: {sum(total_honey)}')
if working_bees:
    print(f"Bees left: {', '.join(str(b) for b in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(n) for n in nectar)}")



