def part1(lines):
    tot_sum = 0
    yes_list = []
    for line in lines:
        if line == '\n':
            yes_list = list(dict.fromkeys(yes_list))
            tot_sum += len(yes_list)
            yes_list = []
        else:
            line = line.rstrip('\n')
            for c in line:
                yes_list.append(c)
    tot_sum += len(list(dict.fromkeys(yes_list)))
    print(tot_sum)

def counter(yes_list, tot_sum):
    if len(yes_list) == 1:
        tot_sum += len(list(dict.fromkeys(yes_list))[0])
        yes_list = []
    else:
        index = 0
        q = ''.join(map(str, yes_list))
        q = list(dict.fromkeys(q))
        for c in q:
            cnt = 0
            for x in yes_list:
                if c in x:
                    cnt += 1
            if cnt == len(yes_list):
                tot_sum += 1
    return tot_sum

def part2(lines):
    yes_list = []
    tot_sum = 0
    for line in lines:
        if line == '\n':
            tot_sum = counter(yes_list, tot_sum)
            yes_list = []
        else:
            yes_list.append(line.rstrip('\n'))
    if len(yes_list) > 0:
        tot_sum = counter(yes_list, tot_sum)
    print(tot_sum)

with open('input.txt') as f:
    lines = f.readlines()
part1(lines)
part2(lines)