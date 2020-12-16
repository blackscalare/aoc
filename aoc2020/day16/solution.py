import re
def part1(lines):
    cnt = 0
    nearby = []
    n = []
    limits = []
    for line in lines:
        if cnt < 1:
            limits.append(line)
        if line == '':
            cnt += 1
        if cnt > 1:
            if line != '':
                nearby.append(line)

    for l in nearby[1:]:
        l = l.split(',')
        for x in l:
            n.append(int(x))
    nearby = n
    ranges = []
    for k in limits:
        for y in re.split(' |-', k):
            if y.isdigit():
                ranges.append(int(y))
    r = []
    for i in range(0, len(ranges) - 1, 2):
        for j in range(ranges[i], ranges[i+1] + 1):
            r.append(j)
    error_code = 0
    not_valid = []
    valid = []
    for o in nearby:
        if o not in r:
            error_code += o
            not_valid.append(o)
        else:valid.append(o)
    print(error_code)
    return not_valid
def getCols(i, vals):
    d = []
    #print(vals)
    for s in vals:
        #print(s)
        d.append(int(s[i]))
    return d
def part2(lines, not_valid):
    cnt = 0
    nearby = []
    nearbyd = {}
    mine = []
    mined = {}
    limits = {}
    keys = []
    for line in lines:
        if cnt < 1:
            if line != '':
                line = line.replace(' or ', '-')
                sline = re.split(': |-', line)
                #sline = re.split('-', sline)
                key = sline[:1][0][:len(sline[:1][0])]
                #print(key)
                keys.append(key)
                #limits.append(line)
                limits[key] = sline[1:]
        if line == '':
            cnt += 1
        if cnt == 1:
            if line != '':
                mine.append(line)
        if cnt > 1:
            if line != '':
                nearby.append(line.split(','))
    """for i in nearby[1:]:
        for x in i:
            if int(x) in not_valid:
                try:
                    print(i)
                    print(int(x))
                    i.remove(int(x))
                    print(i)
                except:
                    pass"""
    columns = len(nearby[1:][0])
    cols = {}
    for i in range(columns):
        cols[i] = getCols(i, nearby[1:])
    #print(cols[19]) 
    #print(limits)
    for c in cols:
        for u in not_valid:
            if int(u) in cols[c]:
                cols[c] = filter((int(u)).__ne__, cols[c])
                #cols[c].remove(int(u))
        #print(cols[c])
    for k in limits:
        ranges = []
        for y in limits[k]:
            if y.isdigit():
                ranges.append(int(y))
        r = []
        for i in range(0, len(ranges) - 1, 2):
            for j in range(ranges[i], ranges[i+1] + 1):
                r.append(j)
        limits[k] = r
    #print(limits)
    #print(cols)
    #print(cols)
    #print(limits['departure location'])
    mmine = mine[1:][0].split(',')
    for lk in limits:
        #print(limits[lk])
        for colk in cols:
            if all(elem in limits[lk] for elem in cols[colk]):
                print(lk, colk)
    print()

lines = [line.rstrip('\n') for line in open('input.txt')]
#part1(lines)
part2(lines, part1(lines))
