from copy import deepcopy
def rule1(seats):
    fringe_cases = [0, len(seats) - 1, len(seats[0])]
    not_allowed = []
    for i in range(len(seats)):
        rows = seats[i]
        for j in range(len(rows)):
            adj = 0
            #d
            if seats[i][j] == 'L':
                if i != fringe_cases[1]:
                    if seats[i + 1][j] == '#':
                        adj += 1
                    #dr
                    if j < fringe_cases[2]:
                        if seats[i + 1][j + 1] == '#':
                            adj+=1
                    #dl
                    if j != fringe_cases[0]:
                        if seats[i+1][j - 1] == '#':
                            adj += 1
                #r
                if j != fringe_cases[2]:
                    if seats[i][j+1] == '#':
                        adj+=1
                #l
                if j != fringe_cases[0]:
                    if seats[i][j-1] == '#':
                        adj+=1
                #u
                if i != fringe_cases[0]:
                    if seats[i-1][j] == '#':
                        adj+=1
                    #ur
                    if j != fringe_cases[2]:
                        if seats[i-1][j+1] == '#':
                            adj += 1
                    #ul
                    if j != fringe_cases[0]:
                        if seats[i-1][j-1] == '#':
                            adj+=1
            if adj >= 1:
                not_allowed.append([i,j])
    res = ''
    for i in range(len(seats)):
        rows = seats[i]
        for j in range(len(rows)):
            seat = rows[j]
            if seat == 'L' and [i,j] not in not_allowed:
                res += '#'
            else:
                res += seat
        if i < len(seats):
            res += "\n"
    print(res)
    return res.split('\n')[:-1]

def rule2(seats):
    fringe_cases = [0, len(seats) - 1, len(seats[0]) - 1]
    not_allowed = []
    for i in range(len(seats)):
        rows = seats[i]
        for j in range(len(rows)):
            adj = 0
            #d
            if i != fringe_cases[1]:
                if seats[i + 1][j] == '#':
                    adj += 1
                #dr
                if j < fringe_cases[2]:
                    if seats[i + 1][j + 1] == '#':
                        adj+=1
                #dl
                if j != fringe_cases[0]:
                    if seats[i+1][j - 1] == '#':
                        adj += 1
            #r
            if j != fringe_cases[2]:
                if seats[i][j+1] == '#':
                    adj+=1
            #l
            if j != fringe_cases[0]:
                if seats[i][j-1] == '#':
                    adj+=1
            #u
            if i != fringe_cases[0]:
                if seats[i-1][j] == '#':
                    adj+=1
                #ur
                if j != fringe_cases[2]:
                    if seats[i-1][j+1] == '#':
                        adj += 1
                #ul
                if j != fringe_cases[0]:
                    if seats[i-1][j-1] == '#':
                        adj+=1
            if adj > 3:
                if [i,j] not in not_allowed:
                    not_allowed.append([i,j])
    res = ''
    for i in range(len(seats)):
        rows = seats[i]
        for j in range(len(rows)):
            seat = rows[j]
            if seat == '#' and [i,j] in not_allowed:
                res += 'L'
            else:
                res += seat
        if i < len(seats):
            res += "\n"
    return res.split('\n')[:-1]

def rule3(seats):
    fringe_cases = [0, len(seats) - 1, len(seats[0]) - 1]
    not_allowed = []
    for i in range(len(seats)):
        rows = seats[i]
        for j in range(len(rows)):
            adj = 0
            d = dr = dl = r = l = u = ur = ul = False
            #d
            for k in range(1, len(seats) - 1):
                if i != fringe_cases[1] and i + k <= fringe_cases[1]:
                    if not d and seats[i + k][j] == 'L':
                        d = True
                    if not d and seats[i + k][j] == '#':
                        adj += 1
                        #if(i == 1 and j == 8): print('d')
                        d = True
                    #dr
                    if j < fringe_cases[2] and j + k <= fringe_cases[2]:
                        if not dr and seats[i + k][j + k] == 'L':
                            dr = True
                        if not dr and seats[i + k][j + k] == '#' :
                            adj+=1
                            #if(i == 1 and j == 8): print('dr')
                            dr = True
                    #dl
                    if j != fringe_cases[0] and j - k >= fringe_cases[0]:
                        if not dl and seats[i+k][j - k] == 'L':
                            dl = True
                        if not dl and seats[i+k][j - k] == '#' :
                            adj += 1
                            #if(i == 1 and j == 8): print('dl')
                            dl = True
                #r
                if j != fringe_cases[2] and k+j <= fringe_cases[2]:
                    if not r and seats[i][j+k] == 'L':
                        r = True
                    if not r and seats[i][j+k] == '#':
                        adj+=1
                        #if(i == 1 and j == 8): print('r')
                        r = True
                #l
                if j != fringe_cases[0] and j - k >= fringe_cases[0]:
                    if not l and seats[i][j-k] == 'L':
                        l = True
                    if not l and seats[i][j-k] == '#':
                        adj+=1
                        #if(i == 1 and j == 8): print('l')
                        l = True
                #u
                if i != fringe_cases[0] and i - k >= fringe_cases[0]:
                    if not u and seats[i-k][j] == 'L':
                        u = True
                    if not u and seats[i-k][j] == '#':
                        adj+=1
                        #if(i == 1 and j == 8): print('u')
                        u = True
                    #ur
                    if j != fringe_cases[2] and j + k <= fringe_cases[2] :
                        if not ur and seats[i-k][j+k] == 'L':
                            ur = True
                        if not ur and seats[i-k][j+k] == '#':
                            adj += 1
                            #if(i == 1 and j == 8): print('ur')
                            ur = True
                    #ul
                    if j != fringe_cases[0] and j - k >= fringe_cases[0]:
                        if not ul and seats[i-k][j-k] == 'L':
                            ul = True
                        if not ul and seats[i-k][j-k] == '#':
                            adj+=1
                            #if(i == 1 and j == 8): print('ul')
                            ul = True
            if adj >= 1:
                if [i,j] not in not_allowed:
                    not_allowed.append([i,j])
    res = ''
    for i in range(len(seats)):
        rows = seats[i]
        for j in range(len(rows)):
            seat = rows[j]
            if seat == 'L' and [i,j] not in not_allowed:
                res += '#'
            else:
                res += seat
        if i < len(seats):
            res += "\n"
    #print(res)
    return res.split('\n')[:-1]

def rule4(seats):
    fringe_cases = [0, len(seats) - 1, len(seats[0]) - 1]
    not_allowed = []
    for i in range(len(seats)):
        rows = seats[i]
        
        for j in range(len(rows)):
            adj = 0
            d = dr = dl = r = l = u = ur = ul = False
            #d
            for k in range(1, len(seats) - 1):
                if i != fringe_cases[1] and i + k <= fringe_cases[1]:
                    if not d and seats[i + k][j] == 'L':
                        d = True
                    if not d and seats[i + k][j] == '#':
                        adj += 1
                        #if(i == 1 and j == 8): print('d')
                        d = True
                    #dr
                    if j < fringe_cases[2] and j + k <= fringe_cases[2]:
                        if not dr and seats[i + k][j + k] == 'L':
                            dr = True
                        if not dr and seats[i + k][j + k] == '#' :
                            adj+=1
                            #if(i == 1 and j == 8): print('dr')
                            dr = True
                    #dl
                    if j != fringe_cases[0] and j - k >= fringe_cases[0]:
                        if not dl and seats[i+k][j - k] == 'L':
                            dl = True
                        if not dl and seats[i+k][j - k] == '#' :
                            adj += 1
                            #if(i == 1 and j == 8): print('dl')
                            dl = True
                #r
                if j != fringe_cases[2] and k+j <= fringe_cases[2]:
                    if not r and seats[i][j+k] == 'L':
                        r = True
                    if not r and seats[i][j+k] == '#':
                        adj+=1
                        #if(i == 1 and j == 8): print('r')
                        r = True
                #l
                if j != fringe_cases[0] and j - k >= fringe_cases[0]:
                    if not l and seats[i][j-k] == 'L':
                        l = True
                    if not l and seats[i][j-k] == '#':
                        adj+=1
                        #if(i == 1 and j == 8): print('l')
                        l = True
                #u
                if i != fringe_cases[0] and i - k >= fringe_cases[0]:
                    if not u and seats[i-k][j] == 'L':
                        u = True
                    if not u and seats[i-k][j] == '#':
                        adj+=1
                        #if(i == 1 and j == 8): print('u')
                        u = True
                    #ur
                    if j != fringe_cases[2] and j + k <= fringe_cases[2] :
                        if not ur and seats[i-k][j+k] == 'L':
                            ur = True
                        if not ur and seats[i-k][j+k] == '#':
                            adj += 1
                            #if(i == 1 and j == 8): print('ur')
                            ur = True
                    #ul
                    if j != fringe_cases[0] and j - k >= fringe_cases[0]:
                        if not ul and seats[i-k][j-k] == 'L':
                            ul = True
                        if not ul and seats[i-k][j-k] == '#':
                            adj+=1
                            #if(i == 1 and j == 8): print('ul')
                            ul = True
            if adj > 4:
                if [i,j] not in not_allowed:
                    not_allowed.append([i,j])
    res = ''
    for i in range(len(seats)):
        rows = seats[i]
        for j in range(len(rows)):
            seat = rows[j]
            if seat == '#' and [i,j] in not_allowed:
                res += 'L'
            else:
                res += seat
        if i < len(seats):
            res += "\n"
    #print(res)
    return res.split('\n')[:-1]

def part1(seats):
    last_seats = []
    index = 0
    while True:
        seats = rule1(seats)
        seats = rule2(seats)
        if seats == last_seats:
            break
        last_seats = deepcopy(seats)
        index += 1
    tot = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                tot += 1
    return tot
def part2(seats):
    last_seats = []
    index = 1
    while True:
        print('index',index)
        seats = rule3(seats)
        #print('\n')
        seats = rule4(seats)
        if seats == last_seats:
            break
        last_seats = deepcopy(seats)
        index += 1
        
    tot = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                tot += 1
    return tot
seats = [line.rstrip('\n') for line in open('input.txt')]
saved_index = []
allowed = []
#print(part1(seats))
print(part2(seats))
