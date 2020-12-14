import re
import copy
from itertools import combinations, permutations, compress, product

def convertToBinaryString(dec):
    return format(dec, '036b')

def part1(lines):
    mask = ''
    tmp_mem = list('000000000000000000000000000000000000')
    memory = {}
    for line in lines:
        if line[0].rstrip(' ') == 'mask':
            mask = list(line[1][1:])
        if line[0][:3].rstrip(' ') == 'mem':
            address = int(re.search(r'\d+', line[0]).group())
            val = list(str(convertToBinaryString(int(line[1]))))
            for i in range(len(val)):
                if mask[i] == 'X':
                    tmp_mem[i] = val[i]
                elif mask[i] == '0':
                    tmp_mem[i] = '0'
                elif mask[i] == '1':
                    tmp_mem[i] = '1'
            memory[address] = copy.deepcopy(tmp_mem)
    tot = 0
    for c in memory:
        string = ''
        for x in memory[c]:
            string += x
        tot += int(string, 2)
    print(tot)

def get_addresses(val, memval):
    tmp = copy.deepcopy(val)
    occurances = val.count('X')
    combos = list(product(range(0, 2), repeat=occurances))
    addresses = {}
    tot = 0
    for x in combos:
        string = ''
        valin = 0
        index = 0
        for z in val:
            if z =='X':
                tmp[index] = str(x[valin])
                valin += 1
            index += 1
        string = ''
        for c in tmp:
            string += c
        addresses[int(string, 2)] = memval
    return addresses


def part2(lines):
    mask = ''
    tmp_mem = list('000000000000000000000000000000000000')
    memory = {}
    addresses = {}
    tot = 0
    for line in lines:
        if line[0].rstrip(' ') == 'mask':
            mask = list(line[1][1:])
        if line[0][:3].rstrip(' ') == 'mem':
            address = int(re.search(r'\d+', line[0]).group())
            val = list(str(convertToBinaryString(int(address))))
            val2 = int(line[1])
            for i in range(len(val)):
                if mask[i] == 'X':
                    tmp_mem[i] = 'X'
                elif mask[i] == '0':
                    tmp_mem[i] = val[i]
                elif mask[i] == '1':
                    tmp_mem[i] = '1'
            addresses.update(get_addresses(copy.deepcopy(tmp_mem), val2))

    for c in addresses:
        tot += addresses[c]
    print(tot)

lines = [line.rstrip('\n') for line in open('input.txt')]

lines = [line.split('=') for line in lines]
part1(lines)
part2(lines)
