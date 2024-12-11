input = "125 17"
input = "5 89749 6061 43 867 1965860 0 206250"
stones = [int(x) for x in input.split(" ")]

def get_stone_result(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        stone_len = len(stone_str)
        return [int(stone_str[0:stone_len / 2]), int(stone_str[stone_len / 2:])]
    return [stone * 2024]

stone_map = {}

for stone in stones:
    stone_map[stone] = 1

for i in range(75):
    new_stone_map = {}
    for stone in stone_map:
        for new_stone in get_stone_result(stone):
            if new_stone not in new_stone_map:
                new_stone_map[new_stone] = 0
            new_stone_map[new_stone] += stone_map[stone]
    
    stone_map = new_stone_map

stones = 0

for stone in stone_map:
    stones += stone_map[stone]

print(stones)