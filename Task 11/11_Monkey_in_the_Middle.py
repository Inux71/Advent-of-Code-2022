from itertools import groupby


class Monkey:
    def __init__(self, name: str, items: list, test: list, divider: int, actions: list) -> None:
        self.name: str = name
        self.items: list = items
        self.test: list = test
        self.divider: int = divider
        self.actions: list = actions
        self.inspected_items: int = 0

    def __str__(self) -> str:
        return f"{self.name} {[item for item in self.items]} {[t for t in self.test]} {self.divider} {[a for a in self.actions]} {self.inspected_items}"

    def show_inspected(self) -> str:
        return f"{self.name} inspected items {self.inspected_items} times."

def load_data(filename: str) -> list:
    file = open(filename, 'r')
    data = [line.strip() for line in file]
    data = [list(sub) for element, sub in groupby(data, key=bool) if element]
    file.close()

    monkeys = [Monkey(name=monkey[0], items=[int(i) for i in monkey[1].split()], test=[t for t in monkey[2].split()], divider=int(monkey[3]), actions=[int(a) for a in monkey[4].split()]) for monkey in data]

    return monkeys


monkeys = load_data("Task 11/input_11.txt")

# Part 1

for r in range(20):
    for m in range(len(monkeys)):
        for i in range(len(monkeys[m].items)):
            if i >= len(monkeys[m].items):
                i -= i

            level = monkeys[m].items[i] if monkeys[m].test[1] == 'old' else int(monkeys[m].test[1])
            new = monkeys[m].items[i] * level if monkeys[m].test[0] == '*' else monkeys[m].items[i] + level
            new //= 3

            if new % monkeys[m].divider == 0:
                monkeys[monkeys[m].actions[0]].items.append(new)

            else:
                monkeys[monkeys[m].actions[1]].items.append(new)

            monkeys[m].items.pop(i)
            monkeys[m].inspected_items += 1

times = []

for monkey in monkeys:
    times.append(monkey.inspected_items)

times.sort(reverse=True)

print(times[0] * times[1])

# Part 2

lcm = 1

for monkey in monkeys:
    lcm *= monkey.divider

for r in range(10000):
    for m in range(len(monkeys)):
        for i in range(len(monkeys[m].items)):
            if i >= len(monkeys[m].items):
                i -= i

            level = monkeys[m].items[i] if monkeys[m].test[1] == 'old' else int(monkeys[m].test[1])
            new = monkeys[m].items[i] * level if monkeys[m].test[0] == '*' else monkeys[m].items[i] + level
            new %= lcm

            if new % monkeys[m].divider == 0:
                monkeys[monkeys[m].actions[0]].items.append(new)

            else:
                monkeys[monkeys[m].actions[1]].items.append(new)

            monkeys[m].items.pop(i)
            monkeys[m].inspected_items += 1

times = []

for monkey in monkeys:
    times.append(monkey.inspected_items)

times.sort(reverse=True)

print(times[0] * times[1])