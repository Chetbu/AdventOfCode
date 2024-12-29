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

i = 0
count = 0
while i < len(list_z):
    count += int(value_dict[list_z[i]]*math.pow(2,i))
    i+= 1
print(count)