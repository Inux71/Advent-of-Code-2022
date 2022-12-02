def load_data(filename: str) -> tuple:
    file = open(filename, 'r')
    data = [line.rstrip().split() for line in file]
    file.close()

    for i in range(len(data)):
        if data[i][0] == 'A':
            data[i][0] = 'X'

        elif data[i][0] == 'B':
            data[i][0] = 'Y'

        else:
            data[i][0] = 'Z'
    
    return data


def calculate_points(opponent_move: str, your_move: str) -> int:
    if your_move == 'X':
        if opponent_move == 'X':
            return 4
        
        if opponent_move == 'Y':
            return 1

        if opponent_move == 'Z':
            return 7
    
    if your_move == 'Y':
        if opponent_move == 'X':
            return 8
        
        if opponent_move == 'Y':
            return 5

        if opponent_move == 'Z':
            return 2

    if your_move == 'Z':
        if opponent_move == 'X':
            return 3
        
        if opponent_move == 'Y':
            return 9

        if opponent_move == 'Z':
            return 6


def choose_move(opponent_move: str, round_end: str) -> str:
    if round_end == 'X':
        if opponent_move == 'X':
            return 'Z'
        
        if opponent_move == 'Y':
            return 'X'

        if opponent_move == 'Z':
            return 'Y'

    if round_end == 'Y':
        if opponent_move == 'X':
            return 'X'
        
        if opponent_move == 'Y':
            return 'Y'

        if opponent_move == 'Z':
            return 'Z'

    if round_end == 'Z':
        if opponent_move == 'X':
            return 'Y'
        
        if opponent_move == 'Y':
            return 'Z'

        if opponent_move == 'Z':
            return 'X'


data = load_data("Task 2/input_2.txt")

# Part 1
score = 0

for i in range(len(data)):
    score += calculate_points(data[i][0], data[i][1])

print(score)

# Part 2
score = 0

for i in range(len(data)):
    data[i][1] = choose_move(data[i][0], data[i][1])
    score += calculate_points(data[i][0], data[i][1])

print(score)