from itertools import product

lines = [line.rstrip('\n') for line in open('test_input.txt')]

def check_neighbours(pos, universe):
    to_change = {}         
    count = 0
    directions = list(product([0, 1, -1], repeat=3))
    directions.remove((0,)*3)

    for x, y, z in directions:
        p = (pos[0] + x, pos[1] + y, pos[2] + z)
        try:
            if universe[p] == '#':
                count += 1
        except:
            pass
    #print(count)
    #print(pos, (pos[0], pos[1], pos[2] + 1), (pos[0], pos[1], pos[2] - 1))
    if 1 < count < 4:
        if universe[pos] == '.' and count == 3:
            to_change[pos] = '#'
        elif universe[pos] == '#' and  2 >= count >= 3:
            to_change[pos] = '#'
    else:
        to_change[pos] = '.'
        #to_change[(pos[0],pos[1],pos[2] + 1)] = '.'
        #to_change[(pos[0],pos[1],pos[2] - 1)] = '.'
    return to_change
active = ()
universe = {}
for i in range(0, 6):
    for x in range(10):
        for y in range(10):
            universe[(x, y, i)] = '.'
            universe[(x, y, -i)] = '.'
            universe[(-x, -y, i)] = '.'
            universe[(-x, -y, -i)] = '.'
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        universe[(x, y, 0)] = c


z = 0
while z != 7:
    to_change = {}
    for pos in universe:
        to_change.update(check_neighbours(pos, universe))
    for change in to_change:
        universe[change] = to_change[change]
    for pos in universe:
        for x in range(4):
            for y in range(4):
                if pos == (x, y, 0):
                    
                    print(pos, universe[pos])
    #print('\n\n')
    #if z == 1:
    #    break
    #exit()
    z += 1

line = 0
s = ''
cnt = 0
for pos in universe:
    if universe[pos] == '#':
        cnt += 1

print(cnt)
