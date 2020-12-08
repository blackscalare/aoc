import copy
def part2(instructions):
    
    acc = i = 0
    jmp_pos = []
    nop_pos = []
    for c, inst in enumerate(instructions):
        if inst[:3] == 'jmp':
            jmp_pos.append(c)
        elif inst[:3] == 'nop':
            nop_pos.append(c)
    for x in jmp_pos:
        acc = i = 0
        visited = []
        test = copy.deepcopy(instructions)
        test[x] = 'nop' + test[x][3:]
        #print('c: ', test[x], 'i: ', x)
        while i < len(test):
            if i in visited:
                acc = -1
                break
            instruction = test[i]
            if instruction[:3] == 'acc':
                acc += int(instruction[3:])
            elif instruction[:3] == 'jmp':
                jmp = int(instruction[3:])
                i += jmp
            visited.append(i)
            i += 1
        if acc > 0:
            print(acc)
    prev_acc = 0
    for x in nop_pos:
        acc = i = prev_i = 0
        visited = []
        test = copy.deepcopy(instructions)
        test[x] = 'jmp' + test[x][3:]
        #print('c: ', test[x], 'i: ', x)
        while i < len(test):
            if i in visited:
                acc = -1
                break
            instruction = test[i]
            if instruction[:3] == 'acc':
                acc += int(instruction[3:])
            elif instruction[:3] == 'jmp':
                jmp = int(instruction[3:])
                if jmp == 0:
                    break
                i += jmp - 1
            elif instruction[:3] == 'nop':    
                i += 1
                continue
            visited.append(i)
            prev_i = i
            i += 1
        #if acc == prev_acc:
        #   continue
        if acc > 0:
            print(acc)

def part1(instructions):
    visited = []
    acc = 0
    i = 0
    while i < len(instructions):
        if i in visited:
            break
        instruction = instructions[i]
        if instruction[:3] == 'acc':
            acc += int(instruction[3:])
        elif instruction[:3] == 'jmp':
            jmp = int(instruction[3:])
            i += jmp - 1
        visited.append(i)
        i += 1
    print(acc)

with open('input.txt') as f:
    lines = f.readlines()
instructions = []
for line in lines:
    instructions.append(line.rstrip('\n'))


#part1(instructions)
part2(instructions)
