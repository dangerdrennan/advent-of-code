with open('constants.txt', 'r') as f:
    directions = f.read()
santa_directions = [x for i, x in enumerate(directions) if i % 2 == 0]
robot_directions = [x for i, x in enumerate(directions) if i % 2 == 1]
seen = set()
north_south, east_west = 0, 0
for arrow in santa_directions:
    if arrow == '^':
        north_south += 1
    elif arrow == 'v':
        north_south -= 1
    elif arrow == '<':
        east_west -= 1
    else:
        east_west += 1
    seen.add((north_south, east_west))
north_south, east_west = 0, 0
for arrow in robot_directions:
    if arrow == '^':
        north_south += 1
    elif arrow == 'v':
        north_south -= 1
    elif arrow == '<':
        east_west -= 1
    else:
        east_west += 1
    seen.add((north_south, east_west))
print(len(seen))