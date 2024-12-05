"""
https://adventofcode.com/2024/day/4
"""

"""First puzzle"""

with open("input.txt", "r", encoding='utf-8') as file:
    content = file.read()

lines = content.split("\n")[:-1]

def count_all_xmas(lines):
    rows = len(lines)
    cols = len(lines[0])

    word = "XMAS"
    count = 0

    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-Right
        (-1, -1), # Up-Left
        (1, -1),  # Down-Left
        (-1, 1)   # Up-Right
    ]

    def in_bounds(row, col):
        return 0 <= row < rows and 0 <= col < cols

    for row in range(rows):
        for col in range(cols):
            if lines[row][col] == word[0]:
                for dx, dy in directions:
                    coords = []
                    for i, letter in enumerate(word):
                        r, c = row + i * dx, col + i * dy
                        if not in_bounds(r, c) or lines[r][c] != word[i]:
                            break
                        coords.append((r, c))
                    if len(coords) == len(word):  # Word found
                        count +=1 
    return count

count = count_all_xmas(lines)
print(f"'XMAS' found a total of {count} times.")


"""Second puzzle"""

def count_all_xmas_cross(lines):
    rows = len(lines)
    cols = len(lines[0])

    count = 0

    directions = {
        "down_right": (1, 1),
        "up_right": (-1, 1),
    }

    def in_bounds(row, col):
        return 0 <= row < rows and 0 <= col < cols

    for row in range(rows):
        for col in range(cols):
            if lines[row][col] == "A":
                diag_0, diag_1 = False, False
                for name in ("down_right", "up_right"):
                    dx, dy = directions[name]
                    r, c = row + dx, col + dy
                    counter_r, counter_c = row - dx, col - dy

                    if not in_bounds(r, c) or not in_bounds(counter_r, counter_c):
                        break

                    if (
                        lines[r][c] == "M" and lines[counter_r][counter_c] == "S" or
                        lines[r][c] == "S" and lines[counter_r][counter_c] == "M"
                    ):
                        if name == "down_right":
                            diag_0 = True
                        if name == "up_right":
                            diag_1 = True
                if diag_0 and diag_1:  # Cross found
                    count += 1     
    return count

count = count_all_xmas_cross(lines)
print(f"'X-MAS' found a total of {count} times.")