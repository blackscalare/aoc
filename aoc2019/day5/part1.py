with open('input.txt', 'r') as f:
    ram = f.readlines()
ram = ram[0].split(',')

def operation_add(i, mode):
    #print('Ran add at: {}'.format(i))
    if mode is None:
        ram[int(ram[i+3])] = int(ram[int(ram[i+1])]) + int(ram[int(ram[i+2])])
    else:
        if mode[0] == 0 and mode[1] == 0:
            operation_add(i, None)
        elif mode[0] == 0 and mode[1] == 1:
            ram[int(ram[i+3])] = int(ram[int(ram[i+1])]) + int(ram[i+2])
        elif mode[0] == 1 and mode[1] == 0:
            ram[int(ram[i+3])] = int(ram[i+1]) + int(ram[int(ram[i + 2])])
        elif mode[0] == 1 and mode[1] == 1:
            ram[int(ram[i+3])] = int(ram[i+1]) + int(ram[i+2])

def operation_mul(i, mode):
    #print('Ran mul at: {}'.format(i))
    if mode is None:
        ram[int(ram[i+3])] = int(ram[int(ram[i+1])]) * int(ram[int(ram[i+2])])
    else:
        if mode[0] == 0 and mode[1] == 0:
            operation_add(i, None)
        elif mode[0] == 0 and mode[1] == 1:
            ram[int(ram[i+3])] = int(ram[int(ram[i+1])]) * int(ram[i+2])
        elif mode[0] == 1 and mode[1] == 0:
            ram[int(ram[i+3])] = int(ram[i+1]) * int(ram[int(ram[i + 2])])
        elif mode[0] == 1 and mode[1] == 1:
            ram[int(ram[i+3])] = int(ram[i+1]) * int(ram[i+2])

def operation_input(i):
    ram[int(ram[i + 1])] = input('Enter value: ')

def operation_print(i):
    print(ram[int(ram[i + 1])])

def long_instruction(i):
    instruction = str(ram[i])
    modes = []
    modes.append(int(instruction[1:2]))
    modes.append(int(instruction[:1]))
    if int(instruction[3:]) == 1:
        print(instruction[3:])
        print(instruction)
        operation_add(i, modes)
    elif int(instruction[3:]) == 2:
        operation_mul(i, modes)


for i in range(len(ram)):
    opcode = int(ram[i])
    if i % 2 == 0 or i % 4 == 0:
        if opcode == 1:
            operation_add(i, None)
        elif opcode == 2:
            operation_mul(i, None)
        elif opcode == 3:
            if len(ram[i - 2]) != 4:
                operation_input(i)
        elif opcode == 4:
            if len(ram[i - 2]) != 4 and len(ram[i-4]) != 4:
                operation_print(i)
        elif len(str(opcode)) == 4:
            long_instruction(i)
        elif opcode == 99:
            break
#print(ram)
