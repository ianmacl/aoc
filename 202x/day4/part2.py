with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

print(lines)
pairs = 0

for line in lines:
    (first, second) = line.split(",")
    (first_a, first_b) = [int(x) for x in first.split("-")]
    (second_a, second_b) = [int(x) for x in second.split("-")]
    first_set = set(range(first_a, first_b + 1))
    second_set = set(range(second_a, second_b + 1))
    if len(first_set.intersection(second_set)):
        pairs += 1

print(pairs)
