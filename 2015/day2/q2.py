import math

dimensions = []
with open('constants.txt','r') as f:
    for line in f:
        numbers = line.strip().split('x')
        numbers = [int(x) for x in numbers]
        dimensions.append(numbers)
bow_length = 0
for dimension in dimensions:
    ordered = sorted(dimension)
    bow_length += ordered[0] * 2 + ordered[1] * 2
    bow_length += math.prod(dimension)
print(bow_length)