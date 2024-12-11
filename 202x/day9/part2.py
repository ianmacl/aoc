with open('/Users/imaclennan/build/play/aoc/day9/input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

tail = [0, 0]
head = [0, 0]

entries = [[15, 15] for i in range(0, 10)]


tail_visited = set(['15,15'])

def display(entries):
    min_0 = 0
    max_0 = 30
    min_1 = 0
    max_1 = 30
    for entry in entries:
        min_0 = min(entry[0], min_0)
        max_0 = max(entry[0], max_0)
        min_1 = min(entry[1], min_1)
        max_1 = max(entry[1], max_1)
    for j in range(min_0, max_0 + 1):
        for i in range(min_1, max_1+1):
            char = '.'
            for k in range(0, len(entries)):
                if entries[k][0] == i and entries[k][1] == j:
                    char = str(k)
                    break
            print(char, end='')
        print('')

display(entries)
line_count = 0
for line in lines:
    print('{} - {}'.format(line_count, line))
    (direction, count) = line.split()
    for i in range(0, int(count)):
        if direction == 'R':
            entries[0][0] += 1
        elif direction == 'L':
            entries[0][0] -= 1
        elif direction == 'U':
            entries[0][1] -= 1
        elif direction == 'D':
            entries[0][1] += 1
        
        for j in range(1, 10):
            distance = abs(entries[j][0] - entries[j-1][0]) + abs(entries[j][1] - entries[j-1][1])
            print('Distance between {} and {} is {}'.format(j, j-1, distance))
            if distance == 2:
                # head and tail on same column
                if entries[j][0] == entries[j-1][0]:
                    if entries[j][1] - entries[j-1][1] == 2:
                        entries[j][1] -= 1
                    elif entries[j-1][1] - entries[j][1] == 2:
                        entries[j][1] += 1
                # head and tail on same row
                elif entries[j-1][1] == entries[j][1]:
                    if entries[j][0] - entries[j-1][0] == 2:
                        entries[j][0] -= 1
                    elif entries[j-1][0] - entries[j][0] == 2:
                        entries[j][0] += 1
                else:
                    # diagonal
                    pass
            elif distance == 3:
                if abs(entries[j-1][0] - entries[j][0]) == 1:
                    entries[j][0] = entries[j-1][0]
                    if entries[j-1][1] - entries[j][1] == 2:
                        entries[j][1] += 1
                    else:
                        entries[j][1] -= 1
                elif abs(entries[j-1][1] - entries[j][1]) == 1:
                    entries[j][1] = entries[j-1][1]
                    if entries[j-1][0] - entries[j][0] == 2:
                        entries[j][0] += 1
                    else:
                        entries[j][0] -= 1
            elif distance == 4:
                if entries[j-1][1] - entries[j][1] == 2:
                    entries[j][1] += 1
                else:
                    entries[j][1] -= 1
                if entries[j-1][0] - entries[j][0] == 2:
                    entries[j][0] += 1
                else:
                    entries[j][0] -= 1

        display(entries)
        tail_position = '{},{}'.format(entries[9][0], entries[9][1])
        print(tail_position)
        tail_visited.add(tail_position)

print(tail_visited)
print(len(tail_visited))