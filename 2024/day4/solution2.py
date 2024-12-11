with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

def get_val(i, j):
    if i < 0 or j < 0 or i >= len(data) or j >= len(data[0]):
        return '.'
    return data[i][j]

dirs = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
    [1, 1],
    [-1, -1],
    [1, -1],
    [-1, 1]
]

found = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'X':
            for dir in dirs:
                word = 'X'
                for k in range(1, 4):
                    word += get_val(k*dir[0]+i, k*dir[1]+j)
                if word == 'XMAS':
                    found += 1



print(found)