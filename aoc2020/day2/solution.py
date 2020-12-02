import time
def main():
    with open('stor') as f:
        lines = f.readlines()
    totstart = time.time()
    start = time.time()
    part1(lines)
    end = time.time()
    print('part1 - runtime: {}'.format(end-start))
    start = time.time()
    part2(lines)
    end = time.time()
    print('part2 - runtime: {}'.format(end-start))
    totend = time.time()
    print('total - runtime: {}'.format(totend-totstart))


def part1(lines):
    correctp = 0
    for line in lines:
        line = line.rstrip('\n')
        sline = line.split(' ')
        minv = int(sline[0].split('-')[0])
        maxv = int(sline[0].split('-')[1])
        char = sline[1][0]
        password = sline[2]
        contains = 0
        for c in password:
            if c == char:
                contains += 1
        if contains < minv or contains > maxv:
            pass
        else:
            correctp += 1

    print('part1 - correct passwords: {}'.format(correctp))

def part2(lines):
    correctp = 0
    for line in lines:
        line = line.rstrip('\n')
        sline = line.split(' ')
        first_pos = int(sline[0].split('-')[0])
        second_pos = int(sline[0].split('-')[1])
        char = sline[1][0]
        password = sline[2]
        first_true = password[first_pos - 1] == char
        second_true = password[second_pos - 1] == char
        if first_true and second_true:
            pass
        elif first_true or second_true:
            correctp += 1
    print('part2 - correct passwords: {}'.format(correctp))


if __name__ == "__main__":
    main()
