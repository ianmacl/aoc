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
set_compare = set(['M', 'S'])
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'A':
            set1 = set([get_val(i-1,j-1), get_val(i+1,j+1)])
            set2 = set([get_val(i-1,j+1), get_val(i+1,j-1)])
            if set1 == set_compare and set2 == set_compare:
                found += 1



print(found)