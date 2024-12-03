"""
https://adventofcode.com/2024/day/3
"""
import re

with open("input.txt", "r", encoding='utf-8') as file:
    content = file.read()

def extract_and_sum_muls(content, pattern):
    matches = re.findall(pattern, content)
    try:
        integer_values = [(int(a), int(b)) for a, b in matches]
    except ValueError:
        integer_values = []
        enable = True
        for a, b, do, dont in matches:
            if do:
                enable = True
            if dont:
                enable = False
            if a and b and enable:
                integer_values += [(int(a), int(b))]
    
    return sum([int0*int1 for int0, int1 in integer_values])

"""First puzzle"""
pattern1 = re.compile(r"mul\((\d+),(\d+)\)")
part1 = extract_and_sum_muls(content, pattern1)
print(part1)

"""Second puzzle"""
pattern2 = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))")
part2 = extract_and_sum_muls(content, pattern2)
print(part2)