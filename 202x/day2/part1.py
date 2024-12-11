with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]
print(data)

score = 0

move_map = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

for line in data:
    (opponent, me) = line.split()
    round_score = 0
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