with open('input.txt') as f:
    map = [line.strip() for line in f.readlines()]

points = set()
direction = 'U'
x = 0
y = 0

direction_map = {
    'U': [0, -1],
    'D': [0, 1],
    'L': [-1, 0],
    'R': [1, 0]
}

ndm = {
    'U': 'R',
    'R': 'D',
    'D': 'L',
    'L': 'U'
}

def get_pos(px, py, pmap):
    if px < 0 or px >= len(pmap[0]) or py < 0 or py >= len(pmap):
        return '.'
    return pmap[py][px]

for i in range(len(map[0])):
    for j in range(len(map)):
        if map[j][i] == '^':
            start_x = i
            start_y = j
            map[j] = map[j].replace('^', '.')

spots = 0

for i in range(len(map[0])):
    for j in range(len(map)):
        map_copy = [str(entry) for entry in map]
        if get_pos(i, j, map_copy) != '.':
            continue

        if i == start_x and j == start_y:
            continue

        map_copy[j] = map_copy[j][0:i] + '#' + map_copy[j][i+1:]

        x = start_x
        y = start_y
        direction = 'U'
        loop = True
        for _ in range(100000):
            if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
                loop = False
                break

            points.add("%d_%d" % (x, y))
            stepper = direction_map[direction]
            next_step = get_pos(x + stepper[0], y + stepper[1], map_copy)
            if next_step == '.':
                x += stepper[0]
                y += stepper[1]
            else:
                direction = ndm[direction]

        if loop:
            print("%d_%d" % (i, j))
            spots += 1

print(spots)
#print(len(points))
