def get_prems(i):
    return lines[i-25:i]
def get_sums(i):
    sums = []
    prems = get_prems(i)
    x = y = 0
    for x in range(len(prems)):
        for y in range(len(prems)):
            if x == y:
                pass
            else:
                if prems[x] + prems[y] not in sums:
                    sums.append(prems[x] + prems[y])
    return sums

def part1(lines):
    for i in range(len(lines)):
        if i + 25 > len(lines):
            break
        if i >= 25:
            sums = get_sums(i)
            if lines[i] not in sums:
                return lines[i]
                
def part2(num, lines):
    for i in range(len(lines)):
        if i + 25 > len(lines):
            break
        if i >= 25:
            prems = get_prems(i)
            tot = 0
            checked = []
            for x in prems:
                tot += x
                checked.append(x)
                if tot == num:
                    checked.sort()
                    return checked[:1][0] + checked[len(checked) - 1:][0]

lines = [int(line.rstrip('\n')) for line in open('input.txt')]
part1a = part1(lines)
print(part1a)
print(part2(part1a, lines))
