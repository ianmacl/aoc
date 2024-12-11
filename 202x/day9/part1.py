with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

tail = [0, 0]
head = [0, 0]

tail_visited = set(['0,0'])

for line in lines:
    print(line)
    (direction, count) = line.split()
    for i in range(0, int(count)):
        if direction == 'R':
            head[0] += 1
        elif direction == 'L':
            head[0] -= 1
        elif direction == 'U':
            head[1] -= 1
        elif direction == 'D':
            head[1] += 1
        
        distance = abs(head[0] - tail[0]) + abs(head[1] - tail[1])
        print(distance)
        if distance == 2:
            # head and tail on same column
            if head[0] == tail[0]:
                if tail[1] - head[1] == 2:
                    tail[1] -= 1
                elif head[1] - tail[1] == 2:
                    tail[1] += 1
            # head and tail on same row
            elif head[1] == tail[1]:
                if tail[0] - head[0] == 2:
                    tail[0] -= 1
                elif head[0] - tail[0] == 2:
                    tail[0] += 1
            else:
                # diagonal
                pass
        elif distance == 3:
            if abs(head[0] - tail[0]) == 1:
                tail[0] = head[0]
                if head[1] - tail[1] == 2:
                    tail[1] += 1
                else:
                    tail[1] -= 1
            elif abs(head[1] - tail[1]) == 1:
                tail[1] = head[1]
                if head[0] - tail[0] == 2:
                    tail[0] += 1
                else:
                    tail[0] -= 1

        head_position = '{},{}'.format(head[0], head[1])
        tail_position = '{},{}'.format(tail[0], tail[1])
        print(head_position)
        print(tail_position)
        tail_visited.add(tail_position)

print(tail_visited)
print(len(tail_visited))