with open("input.txt") as f:
    rows = [x.strip() for x in f.readlines()]

def find_ants(f):
    ants = []
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if rows[r][c] == f:
                ants.append([r, c])
    return ants

len_r = len(rows)
len_c = len(rows[0])

anti_nodes = set()

def add_anti(r, c):
    if r >= 0 and c >= 0 and r < len_r and c < len_c:
        anti_nodes.add("%s_%s" % (r, c))

def get_pos(r, c):
    if r < 0 or c < 0 or r >= len_r or c >= len_c:
        return '.'
    return rows[r][c]


for r in range(len(rows)):
    for c in range(len(rows[r])):
        n = get_pos(r, c)
        if n == '.':
            continue
        ants = find_ants(n)
        for ant in ants:
            if ant[0] == r and ant[1] == c:
                continue
            d_r = ant[0] - r
            d_c = ant[1] - c
            add_anti(r - d_r, c - d_c)
            add_anti(r + 2 * d_r, c + 2 * d_c)

print(len(anti_nodes))
