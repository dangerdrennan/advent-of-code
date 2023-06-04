with open('constants.txt', 'r') as f:
    directions = f.read()

north_south, east_west = 0, 0
seen = {}
for arrow in directions:
    if arrow == '^':
        north_south += 1
    elif arrow == 'v':
        north_south -= 1
    elif arrow == '<':
        east_west -= 1
    else:
        east_west += 1
    if tuple([north_south, east_west]) in seen:
        seen[tuple([north_south, east_west])] += 1
    else:
        seen[tuple([north_south, east_west])] = 1
print(len(seen))