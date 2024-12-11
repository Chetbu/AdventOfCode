import math
import copy
import time
import functools
import cProfile

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()
loop_time = start_time


@functools.cache
def apply_rules(stone : int):
    if stone == 0:
        return [1]
    # elif len(str(stone)) % 2 == 0:
    #     s = str(stone)
    #     return [int(s[:int(len(s) / 2)]), int(s[int(len(s) / 2):])]
    elif math.floor(math.log(stone,10)) % 2 == 1:
        multiplication_factor = int(math.pow(10,((math.floor(math.log(10 * stone,10))) / 2)))
        #print(multiplication_factor, stone // multiplication_factor, stone % multiplication_factor)
        return [stone // multiplication_factor, stone % multiplication_factor]
    else:
        return [stone * 2024]

def recursive_fct(stone_t, max_blink):
    if stone_t[1] == max_blink:
        return 1
    else:
        res = apply_rules(stone_t[0])
        temp = 0
        for ele in res:
            temp += recursive_fct((ele, stone_t[1] + 1), max_blink)
        return temp
#print(apply_rules(0), apply_rules(1664), apply_rules(100))

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

init_arr = [(int(x), 0) for x in lines[0].split()]
#init_arr = [(0,0)]
#print(init_arr)


# blink_limit = 35
# current_arr = copy.copy(init_arr)
# count = 0
# count_loop = 0
# i = 0
# while i < len(init_arr):
#     count += recursive_fct(init_arr[i], blink_limit)
#     i += 1



cProfile.run('recursive_fct((0,0), 40)')
