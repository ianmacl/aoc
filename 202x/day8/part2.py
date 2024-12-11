with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

def get_scenic_score(i, j):
    global lines
    tree_height = lines[i][j]
    up_distance = 0
    down_distance = 0
    left_distance = 0
    right_distance = 0
    # up
    for vert in range(i-1, -1, -1):
        up_distance += 1
        if lines[vert][j] >= tree_height:
            break

    # down
    for vert in range(i+1, len(lines)):
        down_distance += 1
        if lines[vert][j] >= tree_height:
            break

    # left
    for horiz in range(j-1, -1, -1):
        left_distance += 1
        if lines[i][horiz] >= tree_height:
            break

    #right
    for horiz in range(j+1, len(lines[i])):
        right_distance += 1
        if lines[i][horiz] >= tree_height:
            break

    return up_distance * down_distance * left_distance * right_distance

max_score = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        max_score = max(get_scenic_score(i, j), max_score)

print(max_score)
