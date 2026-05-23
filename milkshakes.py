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
#         else:
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

def check_numbers(c, m, ch, ml):

    if c > 0 < m:
        ml.appendleft(str(m))
        c -= 5
        ch.append(str(c))

    elif c > 0 > m:
        ch.append(str(c))

    else:
        ml.appendleft(str(m))

chocolates = input().split(", ")
milk = deque(input().split(", "))

milkshakes = 0
have_milkshakes = False

while chocolates and milk:

    chock_num = int(chocolates.pop())
    milk_num = int(milk.popleft())
    if chock_num != milk_num:
        check_numbers(chock_num, milk_num, chocolates, milk)
    elif chock_num > 0 < milk_num:
        milkshakes += 1
        if milkshakes == 5:
            have_milkshakes = True
            break

if have_milkshakes:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(chocolates) or 'empty'}")
print(f"Milk: {', '.join(milk) or 'empty'}")

