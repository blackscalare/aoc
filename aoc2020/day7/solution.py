import re
bags = dict()

def check_bags(bags_w_gold, tot_bags):
    print(len(bags_w_gold))
    kbags = []
    for bag in bags:
        for b in bags[bag]:
            for x in bags_w_gold:
                x = x.rstrip(' ')
                x = x[:(len(x) - 1)]
                if bag == x:
                    continue
                if x in b:
                    kbags.append(bags[bag][0])
    if len(kbags) > 0:
        check_bags(list(dict.fromkeys(kbags)), tot_bags)

def part1(lines):
    tot_bags = 0
    for line in lines:
        line = line.rstrip('.\n')
        line = re.split('contain |, ', line)
        contain = []
        for b in line:
            if b == line[0]:
                pass
            #should work around having else here, otherwise it contains the main bag as well
            contain.append(b)
        bags[line[0].rstrip(' ')] = contain
    bags_w_gold = []
    for bag in bags:
        if bag == 'shiny gold bags':
            continue
        else:
            for b in bags[bag]:
                if 'shiny gold bag' in b:
                    bags_w_gold.append(bags[bag][0])
    tot_bags += len(bags_w_gold)
    check_bags(bags_w_gold, tot_bags)

def check_bags2(bags_in_gold):
    num_bags = 0
    if bags_in_gold[len(bags_in_gold) - 1] != 's':
        bags_in_gold += 's'
    for b in bags[bags_in_gold[2:]]:
        if(b[:1] == 'n'):
            return num_bags
        num_bags += int(b[:1])
        num_bags += check_bags2(b) * int(b[:1])
    return num_bags

def part2(lines):
    tot_bags = 0
    for line in lines:
        line = line.rstrip('.\n')
        line = re.split('contain |, ', line)
        contain = []
        for b in line:
            if b == line[0]:
                pass
            else:
                contain.append(b)
        bags[line[0].rstrip(' ')] = contain
    tot_bags = 0
    bags_in_gold = []
    for bag in bags:
        if bag == 'shiny gold bags':
            for b in bags[bag]:
                yi = int(b[:1])
                tot_bags += yi
                tot_bags += check_bags2(b) * yi
    print(tot_bags)

def main():
    with open('test_input.txt') as f:
        lines = f.readlines()
    for line in lines:
        line = line.rstrip('.\n')
        line = re.split('contain |, ', line)
        contain = []
        for b in line:
            if b == line[0]:
                pass
            else:
                contain.append(b)
            bags[line[0].rstrip(' ')] = contain
    part1(lines)
    part2(lines)



if __name__ == "__main__":
    main()
