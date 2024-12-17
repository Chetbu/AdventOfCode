import math
# import copy
import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

def combo_operand(op, register_dict):
    if 0<= op <= 3:
        return op
    elif op == 4:
        return register_dict['A']
    elif op == 5:
        return register_dict['B']
    elif op == 6:
        return register_dict['C']
    else:
        print('combo error')


def program_router(opcode, operand, register_dict):
    jump_p = True
    if opcode == 0:
        #adv instruction
        numerator = register_dict['A']
        denominator = math.pow(2,combo_operand(operand, register_dict))
        res = int(numerator/denominator)
        register_dict['A'] = res
    elif opcode == 1:
        #bxl instruction
        register_dict['B'] = bitwise_XOR(register_dict['B'], operand)
    elif opcode == 2:
        #bst instruction
        register_dict['B'] = combo_operand(operand,register_dict) % 8
    elif opcode == 3:
        #jnz instruction
        if register_dict['A'] != 0:
            register_dict['pointer'] = operand
            jump_p = False

    elif opcode == 4:
        #bxc instruction
        register_dict['B'] = bitwise_XOR(register_dict['B'], register_dict['C'])
    elif opcode == 5:
        #out instruction
        if 'output' in register_dict:
            register_dict['output'] = register_dict['output'] + ',' + str(combo_operand(operand,register_dict) % 8)
        else:
            register_dict['output'] = str(combo_operand(operand,register_dict) % 8)
    elif opcode == 6:
        #bdv instruction
        numerator = register_dict['A']
        denominator = math.pow(2,combo_operand(operand, register_dict))
        res = int(numerator/denominator)
        register_dict['B'] = res
    elif opcode == 7:
        #cdv instruction
        numerator = register_dict['A']
        denominator = math.pow(2,combo_operand(operand, register_dict))
        res = int(numerator/denominator)
        register_dict['C'] = res
    else:
        print("Error router")
    
    if jump_p:
        register_dict['pointer'] += 2
    return register_dict


def bitwise_XOR(a,b):
    #XOR on the bit
    f_b = bin(max(a,b))
    s_b = bin(min(a,b))

    #print(f_b, s_b)
    i = -1
    res_b = ""
    while s_b[i] != 'b':
        if f_b[i] != s_b[i] and int(f_b[i]) + int(s_b[i]) == 1:
            res_b = '1' + res_b
        else:
            res_b = '0' + res_b
        i -= 1
    #print(f_b[:i+1])
    res_b = f_b[:i+1] + res_b
    return int(res_b, 2)

#print(bitwise_XOR(3,8))        


with open(file_filepath) as f:
    lines = f.read().splitlines()

i = 0
register_dict = {
    'pointer' : 0
}
while i < 3:
    value = int(lines[i].split(': ')[1])
    name = lines[i].split(': ')[0].split(' ')[1]
    #print(name, value)
    register_dict[name] = value
    i += 1

i +=1

program = [int(x) for x in lines[i].split(': ')[1].split(',')]
#print(program)
i = 0
iteration_max = 100
while register_dict['pointer'] + 1 < len(program) and i < iteration_max: 
    p = register_dict['pointer']
    print(i, p)
    i+=1
    register_dict = program_router(program[p], program[p+1], register_dict)

print(register_dict['output'])
