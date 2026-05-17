def adding_nums(nums, set_type):
    for num in nums:
       set_type.add(int(num))

def removing_nums(nums, set_type):
    for num in nums:
        set_type.discard(int(num))

first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))
num_of_commands = int(input())

is_subset = False

for i in range(num_of_commands):
    com = input().split()
    command, set_type, nums = com[0], com[1], com[2:]
    if command == 'Add':
        if set_type == 'First':
            adding_nums(nums, first_set)
        elif set_type == 'Second':
            adding_nums(nums, second_set)

    elif command == 'Remove':
        if set_type == 'First':
            removing_nums(nums, first_set)
        elif set_type == 'Second':
            removing_nums(nums, second_set)

    elif command == 'Check':
        print(first_set <= second_set or second_set <= first_set)

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
