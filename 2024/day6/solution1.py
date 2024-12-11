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

def get_pos(x, y):
    if x < 0 or x == len(map[0]) or y < 0 or y == len(map):
        return '.'
    return map[y][x]

for i in range(len(map[0])):
    for j in range(len(map)):
        if map[j][i] == '^':
            x = i
            y = j
            map[j] = map[j].replace('^', '.')

while x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
    points.add("%d_%d" % (x, y))
    stepper = direction_map[direction]
    next_step = get_pos(x + stepper[0], y + stepper[1])
    if next_step == '.':
        x += stepper[0]
        y += stepper[1]
    else:
        direction = ndm[direction]

print(len(points))
