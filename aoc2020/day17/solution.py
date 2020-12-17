lines = [line.rstrip('\n') for line in open('test_input.txt')]

def check_neighbours(pos, universe):
    to_change = {}
    up_left = (pos[0] - 1, pos[1] - 1, pos[0])
    up = (pos[0], pos[1] - 1, pos[0])
    up_right = (pos[0] + 1, pos[1] - 1, pos[0])
    left = (pos[0] - 1, pos[1], pos[0])
    right = (pos[0] + 1, pos[1], pos[0])
    down_left = (pos[0] - 1, pos[1] + 1, pos[0])
    down = (pos[0], pos[1] + 1, pos[0])
    down_right = (pos[0] + 1, pos[1] + 1, pos[0])

    near_on_z = ((pos[0] - 1, pos[1] + 1, pos[2]), (pos[0], pos[1] + 1, pos[2]), (pos[0] + 1, pos[1] + 1, pos[2]),
                (pos[0] - 1, pos[1], pos[2]),        (),                         (pos[0] + 1, pos[1], pos[2]),
                (pos[0] - 1, pos[1] - 1, pos[2]), (pos[0], pos[1] - 1, pos[2]), (pos[0] + 1, pos[1] - 1, pos[2]))
    near_on_z_up = ((pos[0] - 1, pos[1] + 1, pos[2] + 1), (pos[0], pos[1] + 1, pos[2] + 1), (pos[0] + 1, pos[1] + 1, pos[2] + 1),
                (pos[0] - 1, pos[1], pos[2] + 1),(pos[0], pos[1], pos[2] + 1) , (pos[0] + 1, pos[1], pos[2] + 1),
                (pos[0] - 1, pos[1] - 1, pos[2] + 1), (pos[0], pos[1] - 1, pos[2] + 1), (pos[0] + 1, pos[1] - 1, pos[2] + 1))
    near_on_z_down = ((pos[0] - 1, pos[1] + 1, pos[2] - 1), (pos[0], pos[1] + 1, pos[2] - 1), (pos[0] + 1, pos[1] + 1, pos[2] - 1),
                (pos[0] - 1, pos[1], pos[2] - 1), (pos[0], pos[1], pos[2] - 1), (pos[0] + 1, pos[1], pos[2] - 1),
                (pos[0] - 1, pos[1] - 1, pos[2] - 1), (pos[0], pos[1] - 1, pos[2] - 1), (pos[0] + 1, pos[1] - 1, pos[2] - 1))            
    count = 0
    for near, near_up, near_down in zip(near_on_z, near_on_z_up, near_on_z_down):
        try:
            if universe[near] == '#': 
                count += 1
        except:
            pass
        try:
            if universe[near_up] == '#':
                count += 1
        except:
            pass
        try:
            if universe[near_down] == '#':
                count += 1
        except:
            pass
    #print(count)
    #print(pos, (pos[0], pos[1], pos[2] + 1), (pos[0], pos[1], pos[2] - 1))
    if 1 < count < 4:
        if universe[pos] == '.' and count == 3:
            to_change[pos] = '#'
        elif universe[pos] == '#' and count >= 2 and count <=3:
            to_change[pos] = '#'
        """#if universe[pos] == '.' and count == 3:
        if universe[pos] == '.' and count == 3:
            to_change[pos] = '#'
        if universe[(pos[0], pos[1], pos[2] + 1)] == '.' and count == 3:
                #print([(pos[0],pos[1],pos[2] + 1)])
                to_change[(pos[0],pos[1],pos[2] + 1)] = '#'
        if universe[(pos[0], pos[1], pos[2] - 1)] == '.' and count == 3:
            to_change[(pos[0],pos[1],pos[2] - 1)] = '#'
        elif count >= 2 and count <=3:
            if universe[pos] == '#':
                to_change[pos] = '#'
            #if universe[(pos[0], pos[1], pos[2] + 1)] == '#':
                to_change[(pos[0],pos[1],pos[2] + 1)] = '#'
            #if universe[(pos[0], pos[1], pos[2] - 1)] == '#':
                to_change[(pos[0],pos[1],pos[2] - 1)] = '#'
        else:
            #print([(pos[0],pos[1],pos[2] + 1)])
            to_change[pos] = '.'
            to_change[(pos[0],pos[1],pos[2] + 1)] = '.'
            to_change[(pos[0],pos[1],pos[2] - 1)] = '.'"""
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
while z < 7:
    to_change = {}
    for pos in universe:
        to_change.update(check_neighbours(pos, universe))
    for change in to_change:
        universe[change] = to_change[change]
    for pos in universe:
        for x in range(4):
            for y in range(4):
                if pos == (x, y, -2):
                    pass
                    #print(pos, universe[pos])
    z += 1

line = 0
s = ''
cnt = 0
for pos in universe:
    #print(pos, universe[pos])
    if line % len(universe) == 0:
        s += '\n\n'
        line = 0
    s += universe[pos]
    line += 1
print(s)
for pos in universe:
    if universe[pos] == '#':
        cnt += 1
    #for l in universe[pos]:

print(cnt)
