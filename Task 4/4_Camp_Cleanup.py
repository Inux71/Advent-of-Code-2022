def load_data(filename: str) -> list:
    file = open(filename, 'r')
    data = [line.rstrip().split(',') for line in file]

    for i in range(len(data)):
        data[i] = [data[i][0].split('-'), data[i][-1].split('-')]
        
        data[i][0] = [int(element) for element in data[i][0]]
        data[i][1] = [int(element) for element in data[i][1]]

    file.close()

    return data


def contains_other(first: list, second: list) -> bool:
    f = [i for i in range(first[0], first[-1] + 1)]
    s = [i for i in range(second[0], second[-1] + 1)]

    if first[0] in s and first[-1] in s or second[0] in f and second[-1] in f:
        return True

    return False


def contains_element(first: list, second: list) -> bool:
    f = [i for i in range(first[0], first[-1] + 1)]
    s = [i for i in range(second[0], second[-1] + 1)]

    for i in f:
        if i in s:
            return True

    return False


data = load_data("Task 4/input_4.txt")

# Part 1

count = 0

for arr in data:
    if contains_other(arr[0], arr[-1]):
        count += 1

print(count)

# Part 2

count = 0

for arr in data:
    if contains_element(arr[0], arr[-1]):
        count += 1

print(count)