from itertools import groupby


def load_data(filename: str) -> tuple:
    file = open(filename, 'r')
    data = [line.rstrip() for line in file]
    data = [list(sub) for element, sub in groupby(data, key=bool) if element]
    
    for i in range(len(data)):
        data[i] = [int(element) for element in data[i]]

    return data


data = load_data("Task 1/input_1.txt")

# Part 1
totals = [sum(arr) for arr in data]
print(max(totals))

# Part 2
totals.sort(reverse=True)
top_3 = sum(totals[:3])
print(top_3)