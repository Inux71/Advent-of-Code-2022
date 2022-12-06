def load_data(filename: str) -> str:
    file = open(filename, 'r')
    data = file.readline()
    file.close()

    return data


data = load_data("Task 6/input_6.txt")

# Part 1

for i in range(len(data)):
    chars = data[i:i + 4]
    occurences = [chars.count(c) for c in chars]
    
    if sum(occurences) == 4:
        print(i + 4)
        break

# Part 2

for i in range(len(data)):
    chars = data[i:i + 14]
    occurences = [chars.count(c) for c in chars]
    
    if sum(occurences) == 14:
        print(i + 14)
        break