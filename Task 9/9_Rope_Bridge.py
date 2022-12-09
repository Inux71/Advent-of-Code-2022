def load_data(filename: str) -> list:
    file = open(filename, 'r')
    data = [line.rstrip('\n').split() for line in file]
    file.close()

    return data


def calculate_distance(head: list, tail: list) -> list:
    return [head[0] - tail[0], head[1] - tail[1]]


def sign(val: int) -> int:
    return 0 if val == 0 else 1 if val > 0 else -1


data = load_data("Task 9/input_9.txt")

# Part 1

visited = [[0, 0]]

head = [0, 0]
tail = [0, 0]


for move in data:
    direction: str = move[0]
    distance: int = int(move[1])

    for i in range(distance):
        # Top
        if direction == 'U':
            head[1] -= 1

        # Right
        if direction == 'R':
            head[0] += 1

        # Bottom
        if direction == 'D':
            head[1] += 1

        # Left
        if direction == 'L':
            head[0] -= 1
            
        d = calculate_distance(head=head, tail=tail)

        if abs(d[0]) > 1 or abs(d[1]) > 1:
            tail[0] += sign(d[0])
            tail[1] += sign(d[1])

            t = [tail[0], tail[1]]

            if t not in visited:
                visited.append(t)

print(len(visited))

# Part 2

visited_2 = [[0, 0]]
knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

for move in data:
    direction: str = move[0]
    distance: int = int(move[1])

    for i in range(distance):
        # Top
        if direction == 'U':
            knots[0][1] -= 1

        # Right
        if direction == 'R':
            knots[0][0] += 1

        # Bottom
        if direction == 'D':
            knots[0][1] += 1

       # Left
        if direction == 'L':
            knots[0][0] -= 1

        for j in range(1, len(knots)):
            d = calculate_distance(head=knots[j - 1], tail=knots[j])

            if abs(d[0]) > 1 or abs(d[1]) > 1:
                knots[j][0] += sign(d[0])
                knots[j][1] += sign(d[1])

        t = [knots[-1][0], knots[-1][1]]

        if t not in visited_2:
            visited_2.append(t)

print(len(visited_2))