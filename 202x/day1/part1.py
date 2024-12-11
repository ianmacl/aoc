with open('input1.txt') as f:
    data = [x.strip() for x in f.readlines()]
print(data)
elves = []
current_elf = 0
for line in data:
    if line:
        current_elf += int(line)
    else:
        elves.append(current_elf)
        current_elf = 0
elves.append(current_elf)
print(max(elves))