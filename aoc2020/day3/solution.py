def run(lines, right, down):
    x = 0
    y = down
    hit_trees = 0
    for i in range(down, len(lines), down):
        x = (x + right) % len(lines[0])
        if lines[i][x] == '#':
            hit_trees += 1
    return hit_trees

if __name__ == "__main__":
    lines = tuple(line.rstrip('\n') for line in open('input.txt').readlines())
    print('part1:', run(lines, 3, 1))
    print('part2:', run(lines, 1, 1) * run(lines, 3, 1) * run(lines, 5, 1) * run(lines, 7, 1) * run(lines, 1, 2))
