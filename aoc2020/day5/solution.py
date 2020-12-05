lines = [line.rstrip('\n') for line in open('input.txt').readlines()]
highest = 0
seat_id_list = []

def part2():
    seat_id_list.sort()
    index = 28
    for i in range(len(seat_id_list)):
        if int(seat_id_list[i]) != index:
            print('part2 - missing_seat_id', index)
            return
        index += 1

for line in lines:
    mi = 0
    ma = 127
    row = line[:7]
    seat = line[7:]
    for direction in row:
        if direction == 'F':
            ma = ma - (ma - mi) / 2
        elif direction == 'B':
            mi = mi + (ma - mi) / 2
    row_val = int((ma - mi) + mi)
    mi = 0
    ma = 7
    for direction in seat:
        if direction == 'L':
            ma = int(ma - (ma - mi) / 2)
        elif direction == 'R':
            mi = int(mi + (ma - mi) / 2)
    seat_val = (ma - mi) + mi
    seat_id = int(row_val*8+seat_val)
    seat_id_list.append(seat_id)
    if(seat_id >= highest):
        highest = seat_id
    
part2()
print('part1 - highest_seat_id', highest)