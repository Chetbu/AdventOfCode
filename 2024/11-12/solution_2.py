#import math
import copy
import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

def apply_rules(stone : int):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        return [int(s[:int(len(s) / 2)]), int(s[int(len(s) / 2):])]
    else:
        return [stone * 2024]

#print(apply_rules(0), apply_rules(1664), apply_rules(100))

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

init_arr = [int(x) for x in lines[0].split()]
#print(init_arr)
# create the first dict of value with occurence
dict_value = {}
for ele in init_arr:
    if ele in dict_value:
        dict_value[ele] = dict_value[ele] + 1
    else:
        dict_value[ele] = 1


blink_index = 0
blink_limit = 75


while blink_index < blink_limit:
    blink_index += 1
    new_dict = {}
    for ele in dict_value:
        temp = apply_rules(ele)
        for res in temp:
            if res in new_dict:
                new_dict[res] = new_dict[res] + dict_value[ele]
            else:
                new_dict[res] = dict_value[ele]
    dict_value = new_dict

#eval number of stones
count = 0
for ele in dict_value:
    count += dict_value[ele]

print(count, time.time() - start_time)



