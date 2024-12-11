with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

seen_trees = set()

def add_tree(i, j):
    global seen_trees
    seen_trees.add('{}.{}'.format(i, j))

for i in range(0, len(lines)):
    height = 0
    for j in range(0, len(lines[i])):
        if lines[i][j] > height:
            add_tree(i, j)
            height = lines[i][j]

    height = 0
    for j in range(len(lines[i])-1, -1, -1):
        if lines[i][j] > height:
            add_tree(i, j)
            height = lines[i][j]

for j in range(len(lines[0])-1, -1, -1):
    height = 0
    for i in range(0, len(lines)):
        if lines[i][j] > height:
            add_tree(i, j)
            height = lines[i][j]

    height = 0
    for i in range(len(lines)-1, -1, -1):
        if lines[i][j] > height:
            add_tree(i, j)
            height = lines[i][j]

print(sorted(seen_trees))
print(len(seen_trees))