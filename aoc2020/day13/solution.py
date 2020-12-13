from sympy.ntheory.modular import crt
def part1(lines):
    timestamp = int(lines[:1][0])
    buses_list = lines[1:]
    buses_list = buses_list[0].split(',')
    buses_list = list(filter(lambda a: a != 'x', buses_list))

    time = timestamp
    while True:
        for bus in buses_list:
            b_time = int(bus)
            if time % b_time == 0:
                w_time = time - timestamp
                print(w_time * b_time)
                return
        time += 1
def part2(lines):
    buses_list = lines[1:]
    buses_list = buses_list[0].split(',')
    d = {}
    for i in range(len(buses_list)):
        bus = buses_list[i]
        if bus != 'x':
            d[bus] = i
    time = 0
    p1 = []
    p2 = []
    for bus in d:
        p1.append(int(bus))
        p2.append(-d[bus])
    res = crt(p1, p2)
    print(res[0])
    """while True:
        left = []
        for bus in d:
            b_time = int(bus)
            if (time + d[bus]) % b_time == 0:
                left.append(bus)
            #print(bus)
            #print(d[bus])
        if len(left) == len(d):
            print(time)
            exit()
        print(time)
        time += 1"""
lines = [line.rstrip('\n\r') for line in open('input.txt')]
part1(lines)
part2(lines)