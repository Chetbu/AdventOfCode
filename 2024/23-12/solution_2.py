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

def rec_intersec_connect(arr, dict_connec):
    #print(arr)
    inter_set = set(dict_connec[arr[0]])
    i = 1
    
    while i < len(arr):
        new_ele = arr[i]
        new_inter_set = set(dict_connec[new_ele]) & inter_set
        inter_set = new_inter_set
        i += 1
    return list(inter_set)

def global_rec(computer,dict_connec):
    res = []
    inter_arr = [(computer, x) for x in dict_connec[computer]]
    while len(inter_arr) > 0:
        #print(inter_arr)
        ele = inter_arr.pop(0)
        temp_inter = rec_intersec_connect(ele, dict_connec)
        if len(temp_inter) == 0:
            res.append(ele)
        else:
            for ele_res in temp_inter:
                temp_l = list(ele)
                temp_l.append(ele_res)
                temp_l.sort()
                t = tuple(temp_l)
                #print(t)
                if not(t in inter_arr):
                    inter_arr.append(t)

    return res



with open(file_filepath) as f:
    lines = f.read().splitlines()

connect_dict = {}
#print(lines)
for line in lines:
    sp = line.split('-')
    i = 0
    while i < 2:
        if sp[i] in connect_dict:
            connect_dict[sp[i]] += [sp[-1-i]]
        else:
            connect_dict[sp[i]] = [sp[-1-i]]
        i += 1
computer_l = list(connect_dict.keys())
computer_l.sort()
#print(computer_l)

#print(rec_intersec_connect(('aq','wq','vc'), connect_dict))

#print(global_rec('co', connect_dict))
global_max_l = 0
res = []
for computer in computer_l:
    group_l = global_rec(computer, connect_dict)
    #extract the biggest
    max_l = max([len(x) for x in group_l])
    if max_l > global_max_l:
        global_max_l = max_l
        res = [x for x in group_l if len(x) == max_l]

print(global_max_l, res)
res_string = ""
for c in res[0]:
    res_string += ',' + c

print(res_string[1:])
