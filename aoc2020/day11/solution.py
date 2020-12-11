from copy import deepcopy

def check_seats(seats, allowed):
    row = ''
    lu, u, ru, l, r, ld, d, dr = 0, 0, 0, 0, 0, 0, 0, 0
    fringe_cases = [0, len(seats) - 1, len(seats[0]) - 1]
    _allowed = deepcopy(allowed)
    for i in range(len(seats)):
        rows = seats[i]
        for j in range(len(rows)):
            adj = 0
            #d
            if i != fringe_cases[1]:
                if seats[i + 1][j] == '#' and [i + 1, j] not in allowed:
                    adj += 1
                #dr
                if j < fringe_cases[2]:
                    if seats[i + 1][j + 1] == '#' and [i + 1,j + 1] not in allowed:
                        adj+=1
                #dl
                if j != fringe_cases[0]:
                    if seats[i+1][j - 1] == '#' and [i+1, j - 1] not in allowed:
                        adj += 1
            #r
            if j != fringe_cases[2]:
                if seats[i][j+1] == '#' and [i,j+1] not in allowed:
                    adj+=1
            #l
            if j != fringe_cases[0]:
                if seats[i][j-1] == '#' and [i,j-1] not in allowed:
                    adj+=1
            #u
            if i != fringe_cases[0]:
                if seats[i-1][j] == '#' and [i-1,j] not in allowed:
                    adj+=1
                #ur
                if j != fringe_cases[2]:
                    if seats[i-1][j+1] == '#' and [i-1,j+1] not in allowed:
                        adj += 1
                #ul
                if j != fringe_cases[0]:
                    if seats[i-1][j-1] == '#' and [i-1,j-1] not in allowed:
                        adj+=1
            if adj < 4:
                if [i,j] not in _allowed:
                    _allowed.append([i,j])
    res = ''
    for i in range(len(seats)):
        rows = seats[i]
        for j in range(len(rows)):
            seat = rows[j]
            if seat == '.':
                res += '.'
            elif seat == '#' and [i,j] in _allowed:
                res += '#'
            elif seat == '#' and [i,j] not in _allowed:
                res += 'L'
        if i < len(seats):
            res += "\n"
    allowed = _allowed
    #print(allowed)
    #print(len(allowed))
    #print(seats)
    #for x in seats:
    #    print(x)
   # print(res)
    return res.split('\n')[:-1], _allowed

def fill_seats(seats):

    cnt = 0
    num_seats = 0
    _allowed = []
    for z in seats:
        for k in z:
            if k == 'L':
                num_seats += 1
    s_seats = 0
    while s_seats < num_seats:
        row = ''
        s_seats = 0
        for i in range(len(seats)):
            rows = seats[i]
            for j in range(len(rows)):
                seat = rows[j]
                if seat == 'L':
                    row += '#'
                else:
                    row += seat 
                    #print(c, seat)
            if i < len(seats):
                row += "\n"
        seats, _allowed = check_seats(row.split('\n')[:-1], _allowed)
        for z in seats:
            for k in z:
                if k == '#':
                    s_seats += 1
        print(s_seats, num_seats)
        cnt += 1
    return cnt
seats = [line.rstrip('\n') for line in open('test_input.txt')]
saved_index = []
allowed = []
print(fill_seats(seats))
#print(saved_index)
