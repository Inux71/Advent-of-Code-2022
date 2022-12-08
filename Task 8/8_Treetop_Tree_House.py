def load_data(filename: str) -> list:
    file = open(filename, 'r')
    data = [line.rstrip() for line in file]
    file.close()

    return data


def is_visible(trees: list, tree: str) -> bool:
    if len(trees) == 1:
        if trees[0] >= tree:
            return False

        return True

    trees.sort(reverse=True)

    if trees[0] >= tree:
        return False

    return True


def calculate_score(top: list, right: list, bottom: list, left: list) -> int:
    score = 1

    for trees in [top, right, bottom, left]:
        s = 0

        for i in range(1, len(trees)):
            if trees[i] >= trees[0]:
                s += 1
                break

            s += 1

        score *= s

    return score


data = load_data("Task 8/input_8.txt")

# Part 1
visible_trees = 2 * len(data[0]) + 2 * (len(data) - 2)

for y in range(1, len(data) - 1):
    for x in range(1, len(data[y]) - 1):
        trees = []

        # Top
        for i in range(0, y):
            trees.append(data[i][x])

        if is_visible(trees=trees, tree=data[y][x]):
            visible_trees += 1
            continue

        # Right
        trees = [digit for digit in data[y][x + 1:]]
        
        if is_visible(trees=trees, tree=data[y][x]):
            visible_trees += 1
            continue

        # Bottom
        trees = []

        for i in range(y + 1, len(data)):
            trees.append(data[i][x])

        if is_visible(trees=trees, tree=data[y][x]):
            visible_trees += 1
            continue

        # Left
        trees = [digit for digit in data[y][0:x]]
        
        if is_visible(trees=trees, tree=data[y][x]):
            visible_trees += 1
            continue

print(visible_trees)

# Part 2

scores = []

for y in range(1, len(data) - 1):
    for x in range(1, len(data[y]) - 1):
        # Top
        top_trees = []

        for i in range(0, y + 1):
            top_trees.append(data[i][x])

        top_trees.reverse()

        # Right
        right_trees = [digit for digit in data[y][x:]]

        # Botttom
        bottom_trees = []

        for i in range(y, len(data)):
            bottom_trees.append(data[i][x])

        # Left
        left_trees = [digit for digit in data[y][0:x + 1]]
        left_trees.reverse()

        scores.append(calculate_score(top=top_trees, right=right_trees, bottom=bottom_trees, left=left_trees))

print(max(scores))