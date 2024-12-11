with open('input.txt') as f:
    sacks = [x.strip() for x in f.readlines()]



print(sacks)
priorities = []
for i in range(0, len(sacks), 3):
    (sack1, sack2, sack3) = sacks[i:i+3]
    badge = set(sack1).intersection(set(sack2), set(sack3))

    asc = ord(list(badge)[0])
    if asc < 97:
        priorities.append(asc - ord('@') + 26)
    else:
        priorities.append(asc - ord('`'))
print(sum(priorities))