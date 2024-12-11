with open('/Users/imaclennan/build/play/aoc/day12/input.txt') as f:
    map = [x.strip() for x in f.readlines()]

distances = [
    [10000 for x in range(0, len(map[0]))] for y in range(0, len(map))
]

print(distances)
starting_points = []
for x in range(0, len(map)):
    for y in range(0, len(map[0])):
        if map[x][y] == 'S' or map[x][y] == 'a':
            starting_points.append([x, y])
            distances[x][y] = 0
            start_x = x
            start_y = y
        elif map[x][y] == 'a':
            starting_points.append([x, y])
        elif map[x][y] == 'E':
            end_x = x
            end_y = y

move_options = [[0, 1], [0, -1], [1, 0], [-1, 0]]

x_range = range(0, len(map))
y_range = range(0, len(map[0]))

print(start_x)
print(start_y)
shortest_distance = 1000


changed = True
while changed:
    print('Loop Started')
    changed = False
    #changed = True
    for x in range(0, len(map)):
        for y in range(0, len(map[0])):
            my_character = ord(map[x][y])
            if my_character == 83:
                continue

            my_distance = distances[x][y]

            for move_option in move_options:
                origin_x = x + move_option[0]
                origin_y = y + move_option[1]
                if origin_x in x_range and origin_y in y_range:
                    origin_character = ord(map[origin_x][origin_y])
                    can_move = False
                    if map[x][y] == 'E':
                        if map[origin_x][origin_y] == 'z':
                            can_move = True
                    elif map[x][y] == 'a' and map[origin_x][origin_y] == 'S':
                        can_move = True
                    elif my_character - origin_character <= 1:
                        can_move = True
                    if can_move:
                        new_distance = distances[origin_x][origin_y] + 1

                        if my_distance > new_distance:
                            changed = True
                            print('changed')
                            distances[x][y] = new_distance

print(distances[end_x][end_y])
