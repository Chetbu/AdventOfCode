import math
# import copy
import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()
loop_time = time.time()

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

def evaluate_value_a(value_a, program, program_s, l):
    register_dict = {
        'pointer' : 0,
        'A' : value_a,
        'B' : 0,
        'C' : 0
    }
    while register_dict['pointer'] + 1 < len(program): 
        p = register_dict['pointer']
        register_dict = program_router(program[p], program[p+1], register_dict)
    

    output = register_dict['output']
    if output[-l:] == program_s[-l:]:
        return True
    else:
        return False

def create_3bit_higher_value_array(value):
    i = 0
    r = [value]
    while i < 8:
        r.append(value*8 + i)
        i += 1
    return r

with open(file_filepath) as f:
    lines = f.read().splitlines()

program = [int(x) for x in lines[-1].split(': ')[1].split(',')]

program_s = str(program[0])
i = 1
while i < len(program):
    program_s = program_s + ',' + str(program[i])
    i += 1
output = ""

value_a = 1

highest_value = 1000000
res_arr = []
l_start = 9
found = False

while value_a < highest_value and not(found):
    value_a += 1
    l = l_start
    res_arr = [value_a]
    result_found = True
    while result_found and l < len(program_s) and evaluate_value_a(value_a, program, program_s, l_start):
        result_found = False
        l += 2
        new_arr = []
        while len(res_arr) > 0:
            v = res_arr.pop(0)
            if evaluate_value_a(v, program, program_s, l):
                #create a possible array value to test for a level higher
                new_arr += create_3bit_higher_value_array(v)
                result_found = True
        res_arr = new_arr
        
    if l == len(program_s):
        print(min(res_arr), time.time() - start_time)
        found = True



