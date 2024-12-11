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

def correct_update(update):
    pages = []
    valid = True
    for page_num in range(len(update)):
        page = update[page_num]
        before_pages = order_rules[page] if page in order_rules else []
        for i in range(len(pages)):
            if pages[i] in before_pages:
                new_pages = pages[0:i]
                new_pages.append(page)
                new_pages.extend(pages[i:])
                new_pages.extend(update[page_num+1:])
                return correct_update(new_pages)
        pages.append(page)
        
    return pages    




middle_numbers = []

correct_updates = []

for update in updates:
    pages = []
    valid = True
    for page in update:
        before_pages = order_rules[page] if page in order_rules else []
        for some_page in pages:
            if some_page in before_pages:
                valid = False
        pages.append(page)

    if not valid:
        middle_numbers.append(int(get_middle_number(correct_update(update))))

print(sum(middle_numbers))

