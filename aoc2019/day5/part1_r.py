with open('input.txt', 'r') as f:
    ram = f.readlines()
ram = ram[0].split(',')
def operation_add(i, modes):
    #print('Ran add at: {}'.format(i))
    if modes is None:
        ram[int(ram[i+3])] = int(ram[int(ram[i+1])]) + int(ram[int(ram[i+2])])
    else:
        if modes[0] == 0 and modes[1] == 0:
            operation_add(i, None)
        elif modes[0] == 0 and modes[1] == 1:
            ram[int(ram[i+3])] = int(ram[int(ram[i+1])]) + int(ram[i+2])
        elif modes[0] == 1 and modes[1] == 0:
            ram[int(ram[i+3])] = int(ram[i+1]) + int(ram[int(ram[i + 2])])
        elif modes[0] == 1 and modes[1] == 1:
            ram[int(ram[i+3])] = int(ram[i+1]) + int(ram[i+2])

def operation_mul(i, modes):
    #print('Ran mul at: {}'.format(i))
    if modes is None:
        ram[int(ram[i+3])] = int(ram[int(ram[i+1])]) * int(ram[int(ram[i+2])])
    else:
        if modes[0] == 0 and modes[1] == 0:
            operation_add(i, None)
        elif modes[0] == 0 and modes[1] == 1:
            ram[int(ram[i+3])] = int(ram[int(ram[i+1])]) * int(ram[i+2])
        elif modes[0] == 1 and modes[1] == 0:
            ram[int(ram[i+3])] = int(ram[i+1]) * int(ram[int(ram[i + 2])])
        elif modes[0] == 1 and modes[1] == 1:
            ram[int(ram[i+3])] = int(ram[i+1]) * int(ram[i+2])

def operation_input(i, mode):
    if mode is None:
        ram[int(ram[i + 1])] = input('Enter value: ')
    else:
        ram[i+1] = input('Enter value: ')

def operation_print(i, mode):
    print(mode)
    if mode is None:
        print(ram[int(ram[i + 1])])
    else:
        print(ram[i+1])


ptr = 0
while ram[ptr] != 99:
    instruction = str(ram[ptr])
    n = len(instruction)
    opcode = int(instruction[n - 2:n])
    if len(instruction) > 1:
        modes = str(instruction[:-2])
    else:
        modes = None
    #print(modes)
    if opcode == 1:
        operation_add(ptr, modes)
        ptr += 4
    elif opcode == 2:
        operation_mul(ptr, modes)
        ptr += 4
    elif opcode == 3:
        operation_input(ptr, modes)
        ptr += 2
    elif opcode == 4:
        operation_print(ptr, modes)
        ptr += 2
    elif opcode == 99:
        break
    if ptr >= len(ram):
        break
#
#intcode_comptuer(ram[0].split(','))