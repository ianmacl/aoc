with open('input.txt') as f:
    sacks = [x.strip() for x in f.readlines()]



print(sacks)
priorities = []
for sack in sacks:
    part1 = set(sack[0:len(sack) / 2])
    part2 = set(sack[len(sack) / 2:])
    wrong = part1.intersection(part2)
    asc = ord(list(wrong)[0])
    if asc < 97:
        priorities.append(asc - ord('@') + 26)
    else:
        priorities.append(asc - ord('`'))
print(sum(priorities))