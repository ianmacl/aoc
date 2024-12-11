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
items = []
item_number = 0
total_divisors = 1


for line in lines:
    if line.startswith('Monkey '):
        monkey_result = monkey_regex.match(line)
        monkey = int(monkey_result.group(1))
        monkeys[monkey] = {
            'inspections': 0,
            'items': []
        }
    elif line.startswith('Starting items'):
        items_result = items_regex.match(line)
        monkey_items = [int(x.strip()) for x in items_result.group(1).split(',')]
        for monkey_item in monkey_items:
            items.append({
                'init': monkey_item,
                'operations': []
            })
            monkeys[monkey]['items'].append(item_number)
            item_number += 1
    elif line.startswith('Operation'):
        operation_result = operation_regex.match(line)
        operation = operation_result.group(1)
        monkeys[monkey]['operation'] = operation
    elif line.startswith('Test'):
        test_result = test_regex.match(line)
        test = int(test_result.group(1))
        monkeys[monkey]['test'] = test
        total_divisors *= test
    elif line.startswith('If true'):
        true_result = true_regex.match(line)
        true = int(true_result.group(1))
        monkeys[monkey]['true'] = true
    elif line.startswith('If false'):
        false_result = false_regex.match(line)
        false = int(false_result.group(1))
        monkeys[monkey]['false'] = false


for item in items:
    print(item)
    item['mods'] = [item['init'] % monkeys[monkey]['test'] for monkey in monkeys]

print(total_divisors)
for count in range(0, 10000):
    #print(monkeys)
    #print(sum([len(monkeys[i]['items']) for i in monkeys]))
    
    print(count)
    for i in range(0, len(monkeys)):
        for item_number in monkeys[i]['items']:
            monkeys[i]['inspections'] += 1
            item = items[item_number]
            operation_detail_result = operation_detail_regex.match(monkeys[i]['operation'])
            if not operation_detail_result:
                print("Error!")
                exit()
            op = operation_detail_result.group(2)
            second = operation_detail_result.group(3)
            if op == '*':
                if second == 'old':
                    for monkey in monkeys:
                        test = monkeys[monkey]['test']
                        item['mods'][monkey] = (item['mods'][monkey] * item['mods'][monkey]) % test
                else:
                    second_num = int(second)
                    for monkey in monkeys:
                        test = monkeys[monkey]['test']
                        item['mods'][monkey] = (item['mods'][monkey] * (second_num % test)) % test
            elif op == '+':
                if second == 'old':
                    for monkey in monkeys:
                        test = monkeys[monkey]['test']
                        item['mods'][monkey] = (item['mods'][monkey] + item['mods'][monkey]) % test
                else:
                    second_num = int(second)
                    for monkey in monkeys:
                        test = monkeys[monkey]['test']
                        item['mods'][monkey] = (item['mods'][monkey] + second_num % test) % test

            else:
                exit('Error - bad operation')

            if items[item_number]['mods'][i] == 0:
                monkeys[monkeys[i]['true']]['items'].append(item_number)
            else:
                monkeys[monkeys[i]['false']]['items'].append(item_number)
        
        monkeys[i]['items'] = []


inspections = sorted([monkeys[i]['inspections'] for i in monkeys], reverse=True)
print(inspections[0] * inspections[1])

