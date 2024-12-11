import re

with open('/Users/imaclennan/build/play/aoc/day13/input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

num_regex = re.compile('^([0-9]+).*')


def parse_line(line):
    if line.startswith('['):
        process = line[1:]
        values = []

        has_elements = not process.startswith(']')
        while not process.startswith(']'):
            has_elements = False
            (element, remainder) = parse_line(process)
            values.append(element)

            process = remainder.removeprefix(',')

        return (values, process.removeprefix(']'))
    elif num_regex.match(line):
        result = num_regex.match(line)
        the_num = int(result.group(1))
        remainder = line.removeprefix(result.group(1))
        return (the_num, remainder)


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif not isinstance(left, int) and not isinstance(right, int):
        len_right = len(right)
        for i in range(0, len(left)):
            if i < len_right:
                comp = compare(left[i], right[i])
                if comp != 0:
                    return comp
            else:
                return 1
        
        if len_right > len(left):
            return -1
        return 0
    elif isinstance(left, int):
        return compare([left], right)
    else:
        return compare(left, [right])
     

total = 0
pair = 0
for i in range(0, len(lines), 3):
    pair += 1
    print(pair)
    (left, remainder) = parse_line(lines[i])
    (right, remainder) = parse_line(lines[i+1])
    if compare(left, right) <= 0:
        print('Pair {} is in the right order'.format(pair))
        total += pair
    else:
        print('Pair {} is not in the right order'.format(pair))
    print(total)

print(total)