import math
# import copy
import time
import random
import functools

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)

file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

def gate_calc(gate_t, value_dict):
    gate_type = gate_t[2]
    value_1 = value_dict[gate_t[0]]
    value_2 = value_dict[gate_t[1]]
    output = 0
    if gate_type == 'AND' and value_1 == value_2 == 1:
        output = 1
    elif gate_type == 'OR' and (value_1 == 1 or value_2 == 1):
        output = 1
    elif gate_type == 'XOR' and (value_1 + value_2 == 1):
        output = 1
    #print(gate_t[3])
    value_dict[gate_t[3]] = output
    return value_dict

def gate_permutation(gate_t, permutation_l):
    #return all the permutations
    res = []
    list_permut = []
    output_list = [x[3] for x in gate_t]
    i = 0
    while i < len(permutation_l) - 1:
        j = i + 1
        while j < len(permutation_l):
            #find the gate where the output is the two
            index_i = output_list.index(permutation_l[i])
            index_j = output_list.index(permutation_l[j])
            new_permutation = list(gate_t)
            new_permutation[index_i] = (gate_t[index_i][0], gate_t[index_i][1], gate_t[index_i][2], permutation_l[j])
            new_permutation[index_j] = (gate_t[index_j][0], gate_t[index_j][1], gate_t[index_j][2], permutation_l[i])
            res.append(tuple(new_permutation))
            list_permut.append((permutation_l[i], permutation_l[j]))
            j+= 1
        i += 1
    return res, list_permut

def eval_gates(a,b,gate_t):
    #convert a & b in bytes and in x00 and y00
    offset = int('1' + 50 * '0',2)
    #print('1' + 50 * '0')
    a_bin = bin(a + offset)
    b_bin = bin(b + offset)
    v_dict = {}
    i = 0
    len_b = 45
    while i < len_b:
        if i < 10:
            i_str = '0' + str(i)
        else:
            i_str = str(i)
        v_dict['x' + i_str] = int(a_bin[-1-i])
        v_dict['y' + i_str] = int(b_bin[-1-i])
        i += 1
    #print(v_dict.keys())
    gate_l = list(gate_t)
    n_try = 0
    while len(gate_l) > 0:
        if n_try > 10000:
            #print(n_try)
            return -1
        n_try += 1
        i = 0
        while i < len(gate_l):
            #check if the gate is activated
            current_gate = gate_l[i]
            #print(current_gate)
            if current_gate[0] in v_dict and current_gate[1] in v_dict:
                del gate_l[i]
                v_dict = gate_calc(current_gate, v_dict)
            else:
                i += 1
    list_z = [x for x in list(v_dict.keys()) if x[0] == 'z']
    list_z.sort()
    res_bin = ''
    for ele in list_z:
        res_bin = str(v_dict[ele]) + res_bin
    #print(res_bin)
    return int(res_bin, 2)

def look_for_first_error(gate_t):
    #return the first bit where errors are found
    i = 1
    error_found = False
    while not(error_found):
        ite = 0
        max_test_int = int('1' + i * '0',2)
        while ite < 50 and not(error_found):
            rand_a = random.randint(0,max_test_int)
            rand_b = random.randint(0,max_test_int)
            if eval_gates(rand_a,rand_b,gate_t) != rand_a + rand_b:
                error_found = True
            ite += 1
        if not(error_found):
            i += 1
    print(i, int('1' + i * '0',2), eval_gates(int('1' + i * '0',2),1,gate_t))
    return i

def find_error_and_evaluate_permutation(gate_t):
    #Goal is to find the first problem
    i = look_for_first_error(gate_t)

    #possible gates for a permutation
    possible_gates_permutation = output_scan[i+1] + output_scan[i-1] + output_scan[i]

    #calculate all the possible permutations

    permut_gate_t_arr, permut_name_arr = gate_permutation(gate_t, possible_gates_permutation)
    tries_arr = []
    for ele in permut_gate_t_arr:
        temp = look_for_first_error(ele)
        #print(temp)
        tries_arr.append(temp)
    #print(permut_gate_t_arr)
    print(max(tries_arr))
    index_max_tries = tries_arr.index(max(tries_arr))
    new_gate_t = permut_gate_t_arr[index_max_tries]
    permut = permut_name_arr[index_max_tries]
    
    return new_gate_t, permut


with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

cutoff_i = lines.index('')

gate_l = []
for gates in lines[cutoff_i + 1:]:
    gate_split = gates.split()
    gate_l.append((gate_split[0], gate_split[2], gate_split[1], gate_split[4]))

gate_t= tuple(gate_l)

list_z = [x[3] for x in gate_t if x[3][0] == 'z']
list_z.sort()

#map the gates linked to a z
output_scan = []
already_scanned = []
for z in list_z:
    explore_outputs = [z]
    i = 0
    while i< len(explore_outputs):
        current_output = explore_outputs[i]
        j = 0
        while j < len(gate_t) and gate_t[j][3] != current_output :
            #print(gate_t[j][3], current_output)
            j += 1
        if j < len(gate_t):
            for k in [0,1]:
                if not(gate_t[j][k] in already_scanned):
                    explore_outputs.append(gate_t[j][k])
                    already_scanned.append(gate_t[j][k])
        i += 1
    explore_outputs = [x for x in explore_outputs if x[0] != 'x' and x[0] != 'y']
    output_scan.append(explore_outputs)
#print(output_scan)
#print([len(x) for x in output_scan])


list_permut = []

new_gate_t = gate_t
i = 0
while i < 4:

    new_gate_t, permut = find_error_and_evaluate_permutation(new_gate_t)
    list_permut += list(permut)
    i += 1

list_permut.sort()
res_str = list_permut[0]
i = 1
while i < len(list_permut):
    res_str += ',' + list_permut[i]
    i += 1
print(res_str, time.time() - start_time)

