# from collections import deque
#
# chocolates = [int(ch) for ch in input().split(", ")]
# cups_milk = deque(int(m) for m in input().split(", "))
#
# chocolate_milkshake = 0
# have_milkshakes = False
#
# while chocolates and cups_milk:
#     if chocolates[-1] <= 0 or cups_milk[0] <= 0:
#         if chocolates[-1] <= 0:
#             chocolates.pop(-1)
#         if cups_milk[0] <= 0:
#             cups_milk.popleft()
#     else:
#         if chocolates[-1] == cups_milk[0]:
#             chocolates.pop()
#             cups_milk.popleft()
#             chocolate_milkshake += 1
#             if chocolate_milkshake == 5:
#                 have_milkshakes = True
#                 break
#         elif chocolates[-1] != cups_milk[0]:
#             cups_milk.rotate(1)
#             chocolates[-1] -= 5
#
# if have_milkshakes:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
#
# print(f"Chocolate: {', '.join([str(ch) for ch in chocolates]) or 'empty'}")
# print(f"Milk: {', '.join([str(m) for m in cups_milk]) or 'empty'}")
from collections import deque

chocolates = list(map(int, input().split(", ")))
milk_cup = deque(map(int, input().split(", ")))

milkshakes = 0
is_milkshake = False

while milk_cup and chocolates:
    last_chocolate = chocolates[-1]
    first_milk_cup = milk_cup[0]

    if last_chocolate > 0 < first_milk_cup:
        if last_chocolate == first_milk_cup:
            milkshakes += 1
            chocolates.pop()
            milk_cup.popleft()
            if milkshakes == 5:
                is_milkshake = True
                break
        else:
            milk_cup.rotate(1)
            last_chocolate -= 5
            chocolates[-1] = last_chocolate
    else:
        if last_chocolate <= 0:
            chocolates.pop()
        if first_milk_cup <=0:
            milk_cup.popleft()

if is_milkshake:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(c) for c in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(m) for m in milk_cup) or 'empty'}")
