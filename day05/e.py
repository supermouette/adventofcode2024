from typing import List


with open("input.txt") as f:
    lines = f.readlines()

previous = {}
updates = []
input_first_part = True
for l in lines:
    if l == "\n":
        input_first_part = False
    elif input_first_part:
        a, b = l.strip("\n").split("|")
        a, b = int(a), int(b)
        previous[b] = previous.get(b, []) + [a]
    else:
        updates.append([int(a) for a in l.strip("\n").split(",")])

sum_p1 = 0
wrong_updates = []
for update in updates:
    printed = []
    can_print_update = True
    for page in update:
        page_needed_before = previous.get(page, [])
        for p in page_needed_before:
            if p in update and p not in printed:
                can_print_update = False
                break
        if can_print_update == False:
            break
        printed.append(page)
    if can_print_update:
        sum_p1 += update[len(update) // 2]
    else:
        wrong_updates.append(update)

print(sum_p1)  # part 1

sum_p2 = 0
for update in wrong_updates:
    printed = []
    remaining_pages: List = update[:]
    while len(printed) != len(update):
        # find next page
        for page in remaining_pages:
            can_print = True
            for p in previous.get(page, []):
                if p in update and p not in printed:
                    can_print = False
                    break
            if can_print:
                printed.append(page)
                remaining_pages.remove(page)
                break
    sum_p2 += printed[len(printed) // 2]

print(sum_p2)  # part 2
