import re
import functools

with open('/Users/imaclennan/build/play/aoc/day13/input.txt') as f:
    lines = [x.strip() for x in f.readlines() if x.strip()]

num_regex = re.compile('^([0-9]+).*')
divider_1 = '[[2]]'
divider_2 = '[[6]]'
lines.append(divider_1)
lines.append(divider_2)

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
     
def get_processed_line(line):
    (process_line, remainder) = parse_line(line)
    return process_line

processed_lines = [get_processed_line(line) for line in lines]

sorted_lines = sorted(processed_lines, key=functools.cmp_to_key(compare))

print(sorted_lines)

divider_1_match = str(get_processed_line(divider_1))
divider_2_match = str(get_processed_line(divider_2))

for i in range(0, len(sorted_lines)):
    if str(sorted_lines[i]) == divider_1_match:
        div1 = i + 1
    elif str(sorted_lines[i]) == divider_2_match:
        div2 = i + 1

print(div1 * div2)
