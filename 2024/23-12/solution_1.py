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

i = 0
connect3_arr = []
while i < len(computer_l):
    first_computer = computer_l[i]
    list_connected_computers = connect_dict[first_computer]
    for second_connected_c in list_connected_computers:
        second_connect_l = connect_dict[second_connected_c]
        for third_connected_c in second_connect_l:
            if third_connected_c in list_connected_computers:
                connect_3_l = [first_computer, second_connected_c, third_connected_c]
                connect_3_l.sort()
                connect_3_t = tuple(connect_3_l)
                if not(connect_3_t) in connect3_arr:
                    connect3_arr.append(connect_3_t)
    i += 1

print(connect3_arr)

count = 0
for co in connect3_arr:
    is_t_c = False
    for ele in co:
        if ele[0] == 't':
            is_t_c = True
    if is_t_c:
        count += 1

print(count)