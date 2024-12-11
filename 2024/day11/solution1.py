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

for i in range(25):
    print(stones)
    new_lists = [get_stone_result(stone) for stone in stones]
    stones = []
    for new_list in new_lists:
        stones.extend(new_list)

print(len(stones))