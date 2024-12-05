"""
https://adventofcode.com/2024/day/5
"""

rules = []
updates = []

with open("input.txt", "r", encoding='utf-8') as file:
    in_rules = True
    for line in file:
        line = line.strip()
        if not line:  # Empty line separates rules and updates
            in_rules = False
            continue
        if in_rules:
            # Parse rules as tuples of integers
            rules.append(tuple(map(int, line.split("|"))))
        else:
            # Parse updates and calculate their middle values
            update = tuple(map(int, line.split(",")))
            middle_value = update[len(update) // 2]
            updates.append(update)

def is_ordered(update, rules):
    # Create a dictionary for quick look-up of page indices in the update
    page_index = {page: idx for idx, page in enumerate(update)}

    # Check each rule to see if it's violated
    for x, y in rules:
        if x in page_index and y in page_index:
            if page_index[x] > page_index[y]:  # Rule is violated if X comes after Y
                return False
    return True

def reorder_update(update, rules):
    ordered_update = list(update[:])
    
    for x, y in rules:
        if x in ordered_update and y in ordered_update:
            if ordered_update.index(x) > ordered_update.index(y):
                ix_x, ix_y = ordered_update.index(x), ordered_update.index(y)
                ordered_update[ix_x], ordered_update[ix_y] = ordered_update[ix_y], ordered_update[ix_x]
    
    return ordered_update

def calculate_middle_sum(updates, rules, correct=True):
    middle_values = []

    for update in updates:
        if correct:
            # If the update is in the correct order, add its middle value to the sum
            if is_ordered(update, rules):
                middle = update[len(update) // 2]
                middle_values.append(middle)
        else:
            # If the update is not in the correct order, reorder it and add its middle value
            if not is_ordered(update, rules):
                reordered_update = reorder_update(update, rules)
                middle = reordered_update[len(reordered_update) // 2]
                middle_values.append(middle)

    return sum(middle_values)

part_1 = calculate_middle_sum(updates, rules, correct=True)
print(f"Sum of Correct middle values: {part_1}")

part_2 = calculate_middle_sum(updates, rules, correct=False)
print(f"Sum of middle values of newly ordered values: {part_2}")
