from collections import deque

def negative_result(magic, material):
    return magic + material

def find_zeros(magic, material):
    if magic[0] == 0:
        magic.popleft()
    if material[-1] == 0:
        material.pop()

def check_if_christmas_ready(crafted):
    if "Doll" in crafted.keys() and 'Wooden train' in crafted.keys()  or \
            'Teddy bear' in crafted.keys() and 'Bicycle' in crafted.keys():
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")



box_of_materials = [int(b) for b in input().split()]
magic_level = deque([int(m) for m in input().split()])

presents = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400,
}

crafted_toys = {}
product_operation = 0

while box_of_materials and magic_level:
    product_operation = magic_level[0] *  box_of_materials[-1]
    if  product_operation < 0:
        product_operation = negative_result(box_of_materials[-1], magic_level[0])
        magic_level.popleft()
        box_of_materials.pop()
        box_of_materials.append(product_operation)
    elif product_operation > 0:
        if product_operation in presents.values():
            for k, v in presents.items():
                if product_operation == v:
                    box_of_materials.pop()
                    magic_level.popleft()
                    if k not in crafted_toys:
                        crafted_toys[k] =0
                    crafted_toys[k] += 1
                    break
        else:
            magic_level.popleft()
            box_of_materials[-1] += 15
    else:
        find_zeros(magic_level, box_of_materials)

check_if_christmas_ready(crafted_toys)
print(f"Materials left: {', '.join(str(b) for b in box_of_materials[::-1])}") if box_of_materials else ""
print(f"Magic left: {', '.join(str(m) for m in magic_level)}") if magic_level else ""
for k, v in sorted(crafted_toys.items()):
    print(f'{k}: {v}')