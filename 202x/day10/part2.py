with open('/Users/imaclennan/build/play/aoc/day10/input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

x = 1
signal_measurements = [20, 60, 100, 140, 180, 220]
cycle = 0
signal_strength = 0

def output(cycle, x):
    global signal_strength, signal_measurements
    if cycle in signal_measurements:
        signal_strength += x * cycle
    #print('Cycle {}: {}'.format(cycle, x))
    position = (cycle - 1) % 40
    if abs(position - x) <= 1:
        print('#', end='')
    else:
        print('.', end='')
    if position == 39:
        print('')

for line in lines:
    if line == 'noop':
        cycle += 1
        output(cycle, x)
        
    else:
        (instruction, value) = line.split()
        if instruction == 'addx':
            cycle += 1
            output(cycle, x)
            cycle += 1
            output(cycle, x)
            x += int(value)

print(signal_strength)