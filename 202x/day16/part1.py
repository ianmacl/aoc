import re

line_parser = re.compile('Valve ([A-Z]+) has flow rate=([0-9]+); tunnels? leads? to valves? ([A-Z, ]+)')

with open('/Users/imaclennan/build/play/aoc/day16/input_test.txt') as f:
    lines = [line_parser.match(x.strip()) for x in f.readlines()]

valves = {}

for line in lines:
    info = line.groups()
    print(line.groups())
    valves[info[0]] = {
        'pressure': int(info[1]),
        'rooms': [room.strip() for room in info[2].split(',')],
        'otime': 0
    }

location = 'AA'
visited = set()
time = 30

while time > 0:
    if valves[location]['pressure'] > 0 and location not in visited:
        print('Opening {}'.format(location))
        time -= 1
        valves[location]['otime'] = time
        visited.add(location)
    unopened_valves = sorted([room for room in valves[location]['rooms'] if room not in visited], key=lambda room: valves[room]['pressure'], reverse=True)
    if len(unopened_valves) > 0:
        location = unopened_valves[0]
        time -= 1
    else:
        print('Nowhere to go')
        exit()
    print(unopened_valves)
    

print(valves)
    #print(line)