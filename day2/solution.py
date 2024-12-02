"""
https://adventofcode.com/2024/day/2
"""
left = list()
right = list()

with open("input.txt", "r") as file:
    lines = [[int(y) for y in x.split(" ")] for x in file.readlines()]

def is_safe(level): 
    diff = [level_a - level_b for level_a, level_b in zip(level, level[1:])]
    return len({d > 0 for d in diff}) == 1 and all(1 <= abs(d) <= 3 for d in diff)   

safe_lines_part_a, safe_lines_part_b  = 0, 0
for level in lines:
    safe_lines_part_a += is_safe(level)
    safe_lines_part_b += any(is_safe(level[:i]+level[i+1:]) for i in range(len(level)))
        
print(safe_lines_part_a, safe_lines_part_b)