import math
# import copy
import time
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
            j+= 1
        i += 1
    return res

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

cutoff_i = lines.index('')
#print(cutoff_i)
value_dict = {}
for init_s in lines[:cutoff_i]:
    split_s = init_s.split(': ')
    value_dict[split_s[0]] = int(split_s[1])
#print(value_dict['x00'])
gate_l = []
for gates in lines[cutoff_i + 1:]:
    gate_split = gates.split()
    gate_l.append((gate_split[0], gate_split[2], gate_split[1], gate_split[4], False))

gate_t= tuple(gate_l)
#print(gate_l)
while len(gate_l) > 0:
    i = 0
    while i < len(gate_l):
        #check if the gate is activated
        current_gate = gate_l[i]
        #print(current_gate)
        if current_gate[0] in value_dict and current_gate[1] in value_dict:
            del gate_l[i]
            value_dict = gate_calc(current_gate, value_dict)
        else:
            i += 1

#print(value_dict['z00'])
list_z = [x for x in list(value_dict.keys()) if x[0] == 'z']
list_z.sort()

#calc expected value
list_x = [x for x in list(value_dict.keys()) if x[0] == 'x']
list_y = [x for x in list(value_dict.keys()) if x[0] == 'y']
i = 0
number_x = 0
number_y = 0
while i < len(list_x):
    number_x += int(value_dict[list_x[i]]*math.pow(2,i))
    number_y += int(value_dict[list_y[i]]*math.pow(2,i))
    i+= 1
#print(number_x, number_y)
number_z = bin(number_x + number_y)
#print(number_z)
#compare bit by bit
i = 0
compare_l = []
while i < len(list_z):
    #print(value_dict[list_z[i]], number_z[-i-1])
    compare_l.append(value_dict[list_z[i]] == int(number_z[-i-1]))
    i += 1
print(compare_l)

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
# print(output_scan)
print([len(x) for x in output_scan])

#make the empirical list of possible problem
normal_l = 7
possible_trouble_l = [x for x in output_scan if len(x) != 5]
#print(possible_trouble_l)
possible_trouble_arr = []
i = 2
while i < len(possible_trouble_l) - 1:
    possible_trouble_arr += possible_trouble_l[i]
    i += 1
print(possible_trouble_arr)

#code permutations
print(len(gate_permutation(gate_t, possible_trouble_arr)))

