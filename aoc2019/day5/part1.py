with open('input.txt', 'r') as f:
    ram = f.readlines()
ram = ram[0].split(',')


def operation_add(i):
    ram[int(ram[i+3])] = int(ram[int(ram[i+1])]) + int(ram[int(ram[i+2])])

def operation_mul(i):
    ram[int(ram[i+3])] = int(ram[int(ram[i+1])]) * int(ram[int(ram[i+2])])

def operation_input(i):
    ram[int(ram[i + 1])] = input('Enter value: ')

def operation_print(i):
    print(ram[int(ram[i + 1])])

for i in range(len(ram)):
    opcode = int(ram[i])
    if i % 2 == 0 or i % 4 == 0:
        if opcode == 1:
            operation_add(i)
        elif opcode == 2:
            operation_mul(i)
        elif opcode == 3:
            if len(ram[i - 2]) != 4:
                operation_input(i)
        elif opcode == 4:
            if len(ram[i - 2]) != 4 and len(ram[i-4]) != 4:
                operation_print(i)
        #elif len(str(opcode)) == 4:
         #   print(opcode)
        elif opcode == 99:
            break

#print(ram)