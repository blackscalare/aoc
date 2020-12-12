def part1():
    curr_dir = 'E'
    x = y = 0
    for direction in directions:
        op = direction[:1]
        val = int(direction[1:])
        if op == 'R':
            if val == 90:
                if curr_dir == 'N':curr_dir = 'E'
                elif curr_dir == 'E':curr_dir = 'S'
                elif curr_dir == 'S':curr_dir = 'W'
                elif curr_dir == 'W':curr_dir = 'N'
            elif val == 180:
                if curr_dir == 'N':curr_dir = 'S'
                elif curr_dir == 'E':curr_dir = 'W'
                elif curr_dir == 'S':curr_dir = 'N'
                elif curr_dir == 'W':curr_dir = 'E'
            elif val == 270:
                if curr_dir == 'N':curr_dir = 'W'
                elif curr_dir == 'E':curr_dir = 'N'
                elif curr_dir == 'S':curr_dir = 'E'
                elif curr_dir == 'W':curr_dir = 'S'
        elif op == 'L':
            if val == 90:
                if curr_dir == 'N':curr_dir = 'W'
                elif curr_dir == 'E':curr_dir = 'N'
                elif curr_dir == 'S':curr_dir = 'E'
                elif curr_dir == 'W':curr_dir = 'S'
            elif val == 180:
                if curr_dir == 'N':curr_dir = 'S'
                elif curr_dir == 'E':curr_dir = 'W'
                elif curr_dir == 'S':curr_dir = 'N'
                elif curr_dir == 'W':curr_dir = 'E'
            elif val == 270:
                if curr_dir == 'N':curr_dir = 'E'
                elif curr_dir == 'E':curr_dir = 'S'
                elif curr_dir == 'S':curr_dir = 'W'
                elif curr_dir == 'W':curr_dir = 'N'
        elif op == 'F':
            if curr_dir == 'N':
                y += val
            elif curr_dir == 'S':
                y -= val
            elif curr_dir == 'E':
                x += val
            elif curr_dir == 'W':
                x -= val
        elif op == 'N':
            y += val
        elif op == 'S':
            y -= val
        elif op == 'E':
            x += val
        elif op == 'W':
            x -= val
    return x, y
def part2():
    curr_dir = 'E'
    x = y = 0
    wx = 10
    wy = 1
    for direction in directions:
        op = direction[:1]
        val = int(direction[1:])
        if op == 'R':
            o_wx = wx
            o_wy = wy
            if val == 90:
                if curr_dir == 'N':curr_dir = 'E'
                elif curr_dir == 'E':curr_dir = 'S'
                elif curr_dir == 'S':curr_dir = 'W'
                elif curr_dir == 'W':curr_dir = 'N'
                wx = o_wy
                wy = -o_wx
            elif val == 180:
                if curr_dir == 'N':curr_dir = 'S'
                elif curr_dir == 'E':curr_dir = 'W'
                elif curr_dir == 'S':curr_dir = 'N'
                elif curr_dir == 'W':curr_dir = 'E'
                wx = -o_wx
                wy = -o_wy
            elif val == 270:
                if curr_dir == 'N':curr_dir = 'W'
                elif curr_dir == 'E':curr_dir = 'N'
                elif curr_dir == 'S':curr_dir = 'E'
                elif curr_dir == 'W':curr_dir = 'S'
                wx = -o_wy
                wy = o_wx
        elif op == 'L':
            o_wx = wx
            o_wy = wy
            if val == 90:
                if curr_dir == 'N':
                    curr_dir = 'W'
                elif curr_dir == 'E':
                    curr_dir = 'N'
                elif curr_dir == 'S':
                    curr_dir = 'E'
                elif curr_dir == 'W':
                    curr_dir = 'S'
                wx = -o_wy
                wy = o_wx
            elif val == 180:
                if curr_dir == 'N':
                    curr_dir = 'S'
                elif curr_dir == 'E':
                    curr_dir = 'W'
                elif curr_dir == 'S':
                    curr_dir = 'N'
                elif curr_dir == 'W':
                    curr_dir = 'E'
                wx = -o_wx
                wy = -o_wy
            elif val == 270:
                if curr_dir == 'N':
                    curr_dir = 'E'
                elif curr_dir == 'E':
                    curr_dir = 'S'
                elif curr_dir == 'S':
                    curr_dir = 'W'
                elif curr_dir == 'W':
                    curr_dir = 'N'
                wx = o_wy
                wy = -o_wx
        elif op == 'F':
            x += wx*val
            y += wy*val
        elif op == 'N':
            wy += val
        elif op == 'S':
            wy -= val
        elif op == 'E':
            wx += val
        elif op == 'W':
            wx -= val
    return x, y
directions = [line.rstrip('\n\r') for line in open('input.txt')]
x, y = part1()
print(abs(x) + abs(y))
x, y = part2()
print(abs(x) + abs(y))
