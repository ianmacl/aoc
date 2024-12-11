from math import floor


order_rules = {}
updates = []
section = 0
with open("input.txt") as f:
    for line in f.readlines():
        stripped = line.strip()
        if stripped == "":
            section = 1
            continue
        if section == 0:
            parts = stripped.split("|")
            if parts[0] not in order_rules:
                order_rules[parts[0]] = []
            order_rules[parts[0]].append(parts[1])
        else:
            updates.append(stripped.split(","))

def get_middle_number(update):
    return update[int(floor(len(update)/2))]


middle_numbers = []

for update in updates:
    pages = []
    valid = True
    for page in update:
        before_pages = order_rules[page] if page in order_rules else []
        for some_page in pages:
            if some_page in before_pages:
                valid = False
        pages.append(page)

    if valid:
        middle_numbers.append(int(get_middle_number(update)))

print(sum(middle_numbers))

