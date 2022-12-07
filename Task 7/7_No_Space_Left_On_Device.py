from __future__ import annotations


class Node:
    def __init__(self, parent: Node, path: str, is_file: bool, size: int) -> None:
        self.parent: Node = parent
        self.path: str = path
        self.is_file: bool = is_file
        self.size: int = size
        self.children = []

    def __str__(self) -> str:
        return f"{self.parent}, {self.path}, {self.size}"


def create_filesystem(data: list) -> Node:
    root = Node(None, '/', False, 0)
    current = root

    for line in data:
        l = line.split()

        if l[0] == '$' and l[1] == 'cd':
            if l[2] == '..':
                current = current.parent

            else:
                p = current.path + l[2] if current.path == '/' else current.path + '/' + l[2]

                for child in current.children:
                    if child.path == p:
                        current = child
                        break
        
        elif l[0] == '$' and l[1] == 'ls':
            continue
        
        elif l[0] == 'dir':
            p = current.path + l[1] if current.path == '/' else current.path + '/' + l[1]

            current.children.append(Node(parent=current, path=p, is_file=False, size=0))

        else:
            p = current.path + l[1] if current.path == '/' else current.path + '/' + l[1]

            current.children.append(Node(parent=current, path=p, is_file=True, size=int(l[0])))

    return root


def load_data(filename: str) -> list:
    file = open(filename, 'r')
    data = [line.rstrip('\n') for line in file]
    file.close()

    return data[1:]


def sum_sizes(node: Node, storage: dict) -> int:
    if node is None:
        return 0

    if node.is_file:
        return node.size

    dir_capacity = 0

    for child in node.children:
        dir_capacity += sum_sizes(child, storage=storage)

    storage[node.path] = dir_capacity

    return dir_capacity


data = load_data("Task 7/input_7.txt")
file_system = create_filesystem(data)


# Part 1

max_size = 100000
capacities = {}
total_size = sum_sizes(file_system, capacities)
total = sum([v for v in capacities.values() if v <= max_size])

print(total)

# Part 2

total_space = 70000000
space_for_update = 30000000
free_space = total_space - total_size
needed_space = space_for_update - free_space

capacities = {k: v for k, v in sorted(capacities.items(), key=lambda item: item[1])}

for v in capacities.values():
    if (v >= needed_space):
        print(v)
        break