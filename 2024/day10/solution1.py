with open("input.txt") as f:
    terrain = [x.strip() for x in f.readlines()]

trailheads = []

seen_locs = []

def get_value(j, i):
    if j <0 or i < 0 or j >= len(terrain) or i >= len(terrain[0]):
        return -1
    return int(terrain[j][i])

neighbors = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]

def get_scores(j, i):
    loc_string = "%s_%s" % (j, i)
    if loc_string in seen_locs:
        return []
    seen_locs.append(loc_string)
    start_height = get_value(j, i)
    if start_height == 9:
        return [1]
    scores = []
    for n in neighbors:
        j_n = j + n[0]
        i_n = i + n[1]
        neighbor_height = get_value(j_n, i_n)
        
        if neighbor_height == start_height + 1:
            scores.extend(get_scores(j_n, i_n))

    return scores       
    
total_score = 0

for j in range(len(terrain)):
    for i in range(len(terrain[0])):
        if terrain[j][i] == '0':
            seen_locs = []
            score = sum(get_scores(j, i))
            total_score += score
            trailheads.append({
                'i': i,
                'j': j,
                'score': score
            })

print(total_score)