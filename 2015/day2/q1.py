dimensions = []
with open('constants.txt','r') as f:
    for line in f:
        numbers = line.strip().split('x')
        numbers = [int(x) for x in numbers]
        dimensions.append(numbers)
total = 0
for dimension in dimensions:
    l, w, h = dimension[0], dimension[1], dimension[2]
    total += 2*l*w + 2*w*h + 2*h*l
    total += min([l*w, w*h, h*l])
print(total)
