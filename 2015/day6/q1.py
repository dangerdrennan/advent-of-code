import re
import numpy as np

def parse_instruction(string, grid):
    numbers_pattern = r'\b\d+\b' 
    numbers = re.findall(numbers_pattern, string)
    numbers = [int(x) for x in numbers]
    x1, y1, x2, y2 = numbers
    left, right = min(x1, x2), max(x1, x2)
    up, down = min(y1, y2), max(y1, y2)
    if 'toggle' in string:
        grid[left:right+1, up:down+1] = np.logical_not(grid[left:right+1, up:down+1])
    elif 'on' in string:
        grid[left:right+1, up:down+1] = True
    elif 'off' in string:
        grid[left:right+1, up:down+1] = False
    return grid

grid = np.zeros((1000, 1000), dtype=bool)

with open('constants.txt', 'r') as f:
    for line in f:
        grid = parse_instruction(line, grid)

print(np.count_nonzero(grid))
