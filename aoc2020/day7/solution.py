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
                    #print(bags[bag])
    #print(len(list(dict.fromkeys(kbags))))
    #print(list(dict.fromkeys(kbags)))
    if len(kbags) > 0:
        #print(kbags)
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
        #print(line)
    bags_w_gold = []
    for bag in bags:
        #print(bags[bag])
        if bag == 'shiny gold bags':
            continue
        else:
            for b in bags[bag]:
                if 'shiny gold bag' in b:
                    bags_w_gold.append(bags[bag][0])
                    #print(bags[bag])
    tot_bags += len(bags_w_gold)
    #print(bags_w_gold)
    check_bags(bags_w_gold, tot_bags)
    #print(tot_bags)
    #print(bags.get('shiny gold bags'))

def check_bags2(bags_in_gold, tot_bags):
    bd = []
    for bag in bags:
        for x in bags_in_gold:
            x = ''.join([i for i in x if not i.isdigit()])
            x = x[1:]
            if x == bag:
                bd.append(bags[bag][0])
    #print(bd)
    if bd and bd[0] != 'no other bags':
        tot_bags *= int(bd[0][:1])
        print(bd)
    print(tot_bags)
    if len(bd) > 0:
        check_bags2(bd, tot_bags)
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
    print(bags)
    bags_in_gold = []
    for bag in bags:
        if bag == 'shiny gold bags':
            for b in bags[bag]:
                bags_in_gold.append(bags[bag][0])
    #print(bags_in_gold)
    tot_bags = int(bags_in_gold[0][:1])
    check_bags2(bags_in_gold, tot_bags)
#print(lines)
def main():
    with open('test_input.txt') as f:
        lines = f.readlines()
    #part1(lines)
    part2(lines)



if __name__ == "__main__":
    main()
