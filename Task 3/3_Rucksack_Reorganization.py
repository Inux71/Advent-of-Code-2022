def load_data(filename: str) -> tuple:
    file = open(filename, 'r')
    data = [line.rstrip() for line in file]
    file.close()

    return data


def get_value(item: str) -> int:
    if item.islower():
        return 1 + ord(item) - ord('a')

    else:
        return 27 + ord(item) - ord('A')


def get_common_item(rucksack: str) -> str:
    left, right = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]

    for item in left:
        if item in right:
            return item

    
def get_group_common_item(rucksacks: list) -> str:
    for item in rucksacks[0]:
        if item in rucksacks[1] and item in rucksacks[2]:
            return item
    

data = load_data("Task 3/input_3.txt")

# Part 1

sum = 0

for rucksack in data:
    sum += get_value(get_common_item(rucksack))

print(sum)

# Part 2

sum = 0

for i in range(0, len(data), 3):
    sum += get_value(get_group_common_item([data[i], data[i + 1], data[i + 2]]))

print(sum)