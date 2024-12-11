import re

with open('input.txt') as f:
    lines = [x.removesuffix("\n") for x in f.readlines()]

crate_lines = []
move_lines = []
crates = {}
moves = []

in_moves = False
for line in lines:
    if in_moves:
        move_lines.append(line)
    elif not line:
        in_moves = True
    elif '[' in line:
        crate_lines.append(line)

for crate_line in crate_lines:
    for i in range(0, len(crate_line), 4):
        item = crate_line[i:i+4]
        if item:
            crate_number = i // 4
            if not crate_number in crates:
                crates[crate_number] = []
            if item.strip():
                crates[crate_number].append(item[1:2])

print(crates)
for move_line in move_lines:
    move = re.match(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", move_line)
    count = int(move.group(1))
    source = int(move.group(2))
    target = int(move.group(3))
    crates_to_add = []
    for i in range(0, count):
        crates_to_add.append(crates[source-1].pop(0))

    crates_to_add.reverse()
    for item in crates_to_add:
        crates[target-1].insert(0, item)

message = ""
for crate in crates:
    message += crates[crate][0]
print(crates)
print(message)



    