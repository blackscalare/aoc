from itertools import permutations
import copy
def part1(lines):
    checked = []
    one = three = 0
    last_i = -1
    for i in range(len(lines)):
        #last_i = -1
        for j in range(len(lines)):
            x = lines[i]
            y = lines[j]
            if i == j:
                pass
            elif last_i == i:
                continue
            elif (1 <= y - x < 4) and x < y :
                last_i = i
                checked.append(y)
                if y-x == 3:
                    three += 1
                elif y-x == 1:
                    one += 1
    print(one * three)

def part2(lines):
    one = three = 0
    last_i = -1
    last_x = -1
    rep = 0
    ew = []
    ok = []
    for i in range(len(lines)):
        #last_i = -1
        done = True
        rep = 0
        for j in range(len(lines)):
            x = lines[i]
            y = lines[j]
            if i == j:
                pass
            elif (1 <= y - x < 4) and x < y :
                if(last_i == i):
                    rep += 1
                    if done:
                        ew.append(last_x)
                        done = False
                    ew.append(x)
                last_x = x
                last_i = i
                print(x, y)
        if rep > 0:
            ok.append(rep)
    _tot = 1
    for i in range(len(ok)):
        ok[i] += 1
        _tot += pow(ok[i], ok[i])
    #print(ew)
    print(ok)
    print(_tot)
    print(len(ew))
lines = [int(line.rstrip('\n')) for line in open('test_input.txt')]
lines.append(0)
lines.sort()
lines.append(lines[len(lines) - 1] + 3)
#part1(lines)
part2(lines)
