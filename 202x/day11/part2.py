import json
import re

with open('/Users/imaclennan/build/play/aoc/day11/input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

monkey = '0'

monkey_regex = re.compile('Monkey ([0-9]+):')
items_regex = re.compile('Starting items: ([0-9, ]+)')
operation_regex = re.compile('Operation: (.*)')
operation_detail_regex = re.compile('new = ([0-9a-z]+) ([+*]) ([0-9a-z]+)')
test_regex = re.compile('Test: divisible by ([0-9]+)')
true_regex = re.compile('If true: throw to monkey ([0-9]+)')
false_regex = re.compile('If false: throw to monkey ([0-9]+)')

monkeys = {}
items = {}

for line in lines:
    if line.startswith('Monkey '):
        monkey_result = monkey_regex.match(line)
        monkey = int(monkey_result.group(1))
        monkeys[monkey] = {
            'inspections': 0
        }
    elif line.startswith('Starting items'):
        items_result = items_regex.match(line)
        items = [int(x.strip()) for x in items_result.group(1).split(',')]
        monkeys[monkey]['items'] = items
    elif line.startswith('Operation'):
        operation_result = operation_regex.match(line)
        operation = operation_result.group(1)
        monkeys[monkey]['operation'] = operation
    elif line.startswith('Test'):
        test_result = test_regex.match(line)
        test = int(test_result.group(1))
        monkeys[monkey]['test'] = test
    elif line.startswith('If true'):
        true_result = true_regex.match(line)
        true = int(true_result.group(1))
        monkeys[monkey]['true'] = true
    elif line.startswith('If false'):
        false_result = false_regex.match(line)
        false = int(false_result.group(1))
        monkeys[monkey]['false'] = false


for count in range(0, 10000):
    #print(monkeys)
    #print(sum([len(monkeys[i]['items']) for i in monkeys]))
    
    print(count)
    for i in range(0, len(monkeys)):
        for item_number in range(0, len(monkeys[i]['items'])):
            monkeys[i]['inspections'] += 1
            worry = monkeys[i]['items'][item_number]
            operation_detail_result = operation_detail_regex.match(monkeys[i]['operation'])
            if not operation_detail_result:
                print("Error!")
                exit()
            first = operation_detail_result.group(1)
            op = operation_detail_result.group(2)
            second = operation_detail_result.group(3)
            first_number = worry if first == 'old' else int(first)
            second_number = worry if second == 'old' else int(second)
            if op == '*':
                new_worry = first_number * second_number
            elif op == '+':
                new_worry = first_number + second_number
            else:
                exit('Error - bad operation')
            
            #new_worry //= 3
            if new_worry % monkeys[i]['test'] == 0:
                monkeys[monkeys[i]['true']]['items'].append(new_worry)
            else:
                monkeys[monkeys[i]['false']]['items'].append(new_worry)
        
        monkeys[i]['items'] = []


inspections = sorted([monkeys[i]['inspections'] for i in monkeys], reverse=True)
print(inspections[0] * inspections[1])

