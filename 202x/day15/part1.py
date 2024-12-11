import re

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

line_parser = re.compile('Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)')

rock_map = {}
min_x = 655450
max_x = 655450
min_y = 2013424
max_y = 2013424

def add_beacon(x, y):
    return add_item(x, y, 'B')

def add_sensor(x, y):
    return add_item(x, y, 'S')

def block_space(x, y):
    return add_item(x, y, '#')

def add_item(x, y, item):
    global rock_map
    global min_x
    global min_y
    global max_x
    global max_y

    if y not in rock_map:
        rock_map[y] = {}
    if x in rock_map[y]:
        return False
    rock_map[y][x] = item
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    return True

def print_grid():
    global rock_map
    global min_x
    global min_y
    global max_x
    global max_y

    for y in range(min_y, max_y + 1):
        for x in range(min_x - 2, max_x + 3):
            if y in rock_map and x in rock_map[y]:
                print(rock_map[y][x], end='')
            else:
                print('.', end='')
        print('')

check_line = 2000000
line_count = 0
for line in lines:
    print(line_count)
    line_count += 1
    parsed_line = line_parser.match(line)
    (sensor_x, sensor_y, beacon_x, beacon_y) = (int(parsed_line.group(1)), int(parsed_line.group(2)), int(parsed_line.group(3)), int(parsed_line.group(4)))
    add_sensor(sensor_x, sensor_y)
    add_beacon(beacon_x, beacon_y)
    distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
    for y in range(check_line, check_line + 1):
        remaining_distance = distance - abs(y - sensor_y)
        for x in range(sensor_x - remaining_distance, sensor_x + remaining_distance + 1):
            #print('{},{}'.format(x, y))
            block_space(x, y)

#check_line = 10
no_beacon = 0
for x in range(min_x, max_x + 1):
    if x in rock_map[check_line] and rock_map[check_line][x] == '#':
        no_beacon += 1

#print_grid()
print(no_beacon)
