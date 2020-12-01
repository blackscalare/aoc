def part2(lines):
    for count, line in enumerate(lines):
        for _count, _line in enumerate(lines):
            for xount, xine in enumerate(lines):
                if count == _count and count == xount:
                    pass
                if int(line) + int(_line) + int(xine) == 2020:
                    print('part 2 answer: ', int(line)*int(_line)*int(xine))
                    return

def part1(lines):
    for count, line in enumerate(lines):
        for _count, _line in enumerate(lines):
            if count == _count:
                pass
            if int(line) + int(_line) == 2020:
                print('part 1 answer: ', int(line)*int(_line))
                return

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()