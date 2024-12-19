import math
import copy
import time
import functools

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

@functools.cache
def recur_pattern_check(pattern:str, available_towels_arr:tuple, max_l:int):
    i = 1
    res = 0
    
    if len(pattern) == 0:
        return 1
    while i <= max_l and i <= len(pattern):
        studied_pattern = copy.copy(pattern[:i])
        #print(studied_pattern)
        if studied_pattern in available_towels_arr:
            res +=  recur_pattern_check(pattern[i:], available_towels_arr, max_l)


        i += 1
        # #print(i)

    return res




with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)
count = 0
available_towels_arr = tuple(lines[0].split(', '))
max_t_l = max([len(x) for x in available_towels_arr])
display_arr = lines[2:]
#print(recur_pattern_check('g', available_towels_arr, max_t_l))
i = 0
while i < len(display_arr):
    pattern = display_arr[i]
    #print(recur_pattern_check(pattern, available_towels_arr, max_t_l))
    count += recur_pattern_check(pattern, available_towels_arr, max_t_l)
    i += 1
print(count)