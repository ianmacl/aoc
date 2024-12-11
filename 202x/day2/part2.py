with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]
print(data)

score = 0

move_map = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

win_map = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

lose_map = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

for line in data:
    (opponent, outcome) = line.split()
    round_score = 0
    if outcome == 'X':
        me = lose_map[opponent]
    elif outcome == 'Y':
        me = move_map[opponent]
    else:
        me = win_map[opponent]

    if me == 'X':
        round_score += 1
    elif me == 'Y':
        round_score += 2
    elif me == 'Z':
        round_score += 3

    if move_map[opponent] == me:
        round_score += 3
    elif opponent == 'A' and me == 'Y':
        round_score += 6
    elif opponent == 'B' and me == 'Z':
        round_score += 6
    elif opponent == 'C' and me == 'X':
        round_score += 6
    print(round_score)
    score += round_score

print(score)