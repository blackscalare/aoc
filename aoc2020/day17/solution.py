from itertools import product
from collections import defaultdict

lines = [line.rstrip('\n') for line in open('input.txt')]

def check_neighbours(pos, active):
    tmp_active = []   
    count = 0
    directions = list(product([0, 1, -1], repeat=3))
    directions.remove((0,)*3)
    for x, y, z in directions:
        p = (pos[0] + x, pos[1] + y, pos[2] + z)
        neighbours[p] += 1
        if p in active:
            count += 1
    if count == 2 or count == 3:
        tmp_active.append(pos)
    return tmp_active
active = []
universe = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == '#':
            active.append((x, y, 0))

def removeDuplicates(lst):
    return [t for t in (set(tuple(i) for i in lst))]

z = 0
while z != 6:
    neighbours = defaultdict(int)
    tmp_active = []
    for pos in active:
        tmp_active.extend(check_neighbours(pos, active))
    for n in neighbours:
        if neighbours[n] == 3 and n not in active:
            tmp_active.append(n)
    active = removeDuplicates(tmp_active)
    z += 1


print(len(active))
