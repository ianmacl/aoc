with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

rock_map = {}
min_x = 500
min_y = 0
max_x = 500
max_y = 0
sand = 0

def decode_element(element):
    (x, y) = element.split(',')
    return (int(x), int(y))

def add_rock(x, y):
    add_item(x, y, '#')

def add_sand(x, y):
    add_item(x, y, 'o')

def add_item(x, y, item):
    global rock_map
    global min_x
    global min_y
    global max_x
    global max_y

    if y not in rock_map:
        rock_map[y] = {}
    rock_map[y][x] = item
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

def add_rock(x, y):
    add_item(x, y, '#')

def add_sand(x, y):
    global sand
    add_item(x, y, 'O')
    sand += 1


def draw_line(start_x, start_y, end_x, end_y):
    if start_x != end_x:
        if start_x > end_x:
            for i in range(end_x, start_x + 1):
                add_rock(i, end_y)
        else:
            for i in range(start_x, end_x + 1):
                add_rock(i, end_y)
    else:
        if start_y > end_y:
            for i in range(end_y, start_y + 1):
                add_rock(end_x, i)
        else:
            for i in range(start_y, end_y + 1):
                add_rock(end_x, i)

def print_grid():
    global rock_map
    global min_x
    global min_y
    global max_x
    global max_y

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if y in rock_map and x in rock_map[y]:
                print(rock_map[y][x], end='')
            else:
                print('.', end='')
        print('')

for line in lines:
    elements = line.split(' -> ')
    (start_x, start_y) = decode_element(elements[0])
        
    for element in elements[1:]:
        (end_x, end_y) = decode_element(element)
        draw_line(start_x, start_y, end_x, end_y)
        start_x = end_x
        start_y = end_y

sand_added = True
while sand_added:
    sand_added = False
    current_y = 0
    current_x = 500
    sand_moved = True
    while True:
        if current_y + 1 not in rock_map:
            current_y += 1
        else:
            if current_x not in rock_map[current_y + 1]:
                current_y += 1
            elif current_x - 1 not in rock_map[current_y + 1]:
                current_y += 1
                current_x -= 1
            elif current_x + 1 not in rock_map[current_y + 1]:
                current_y += 1
                current_x += 1
            else:
                add_sand(current_x, current_y)
                sand_added = True
                break
        if current_y > max_y:
            break


print_grid()

print(sand)