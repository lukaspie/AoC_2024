"""
https://adventofcode.com/2024/day/1
"""
left = list()
right = list()

with open("input.txt", "r") as file:
    for line in file:
        l,r = line.split()
        left += [int(l)]
        right += [int(r)]
        
"""First puzzle"""        
        
left_sorted, right_sorted = sorted(left), sorted(right)
        
sim_score = 0

for l,r in zip(left_sorted, right_sorted):
    sim_score += abs(r - l)

print(sim_score)

"""Second puzzle"""

sim_score = 0
for l in left_sorted:
    count = right_sorted.count(l)
    sim_score += l*count
    
print(sim_score)