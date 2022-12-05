from itertools import groupby


def load_data(filename: str) -> tuple[list, list]:
    file = open(filename, 'r')
    f_data = [line.rstrip('\n') for line in file]
    f_data = [list(sub) for key, sub in groupby(f_data, key=bool) if key]
    file.close()

    data, moves = f_data[0], f_data[-1]

    for i in range(len(data)):
        data[i] = data[i].split()

    for i in range(len(moves)):
        moves[i] = moves[i].replace('move ', '').replace('from ', '').replace('to ', '')
        moves[i] = [int(element) for element in moves[i].split()]

    return data, moves


data, moves = load_data("Task 5/input_5.txt")

# Part 1

for i in range(len(moves)):
    for j in range(moves[i][0]):
        data[moves[i][2] - 1].append(data[moves[i][1] - 1].pop())

result = ''

for i in range(len(data)):
    result += data[i][-1]

print(result)

# Part 2

for i in range(len(moves)):
    s = []

    for j in range(moves[i][0]):
        s.append(data[moves[i][1] - 1].pop())
    
    s.reverse()

    for k in s:
        data[moves[i][2] - 1].append(k)

result = ''

for i in range(len(data)):
    result += data[i][-1]

print(result)