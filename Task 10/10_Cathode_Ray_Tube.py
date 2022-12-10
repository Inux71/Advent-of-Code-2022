def load_data(filename: str) -> list:
    file = open(filename, 'r')
    data = [line.rstrip() for line in file]
    file.close()

    return data


def check_cycle(cycle: int, x: int) -> None:
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        strengths.append(cycle * x)


def draw(pixel: int, pos: int) -> str:
    if pos -1 <= pixel <= pos +1:
        return '#'

    return '.'


data = load_data("Task 10/input_10.txt")

# Part 1
x = 1
cycle = 1
strengths = []

for d in data:
    check_cycle(cycle=cycle, x=x)

    if 'addx' in d:
        value = int(d.split()[1])
        cycle += 1

        check_cycle(cycle=cycle, x=x)

        x += value

    cycle += 1

print(sum(strengths))

# Part 2

position = 1
cycle = 1
pictures = []
picture = ''

for d in data:
    if len(picture) == 40:
        pictures.append(picture)
        picture = ''
        cycle = 1

    picture += draw(cycle - 1, position)

    if 'addx' in d:
        value = int(d.split()[1])
        cycle += 1

        if len(picture) == 40:
            pictures.append(picture)
            picture = ''
            cycle = 1

        picture += draw(cycle - 1, position)
        position += value

    cycle += 1

pictures.append(picture)

for p in pictures:
    print(p)