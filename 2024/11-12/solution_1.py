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

blink_index = 0
blink_limit = 75
current_arr = copy.copy(init_arr)
while blink_index < blink_limit:
    blink_index += 1
    new_arr = []
    j = 0
    while j < len(current_arr):
        new_arr += apply_rules(current_arr[j])
        j+= 1
    #print(new_arr)
    current_arr = new_arr
    print(blink_index, time.time() - start_time)

print(len(current_arr))
