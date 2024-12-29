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

#print(lines)
lock_arr = []
key_arr = []
i = 0
while i < len(lines):
    if lines[i] == '#####':
        #it is a lock
        res_arr = []
        l_max = 5
        j = 0
        while j < 5:
            l = 1
            while l <= l_max and lines[i + l][j] == '#':
                l += 1
            res_arr.append(l-1)
            j += 1
        #print('lock', res_arr)
        lock_arr.append(res_arr)
    elif lines[i + 6] == '#####':
        #it is a key
        res_arr = []
        l_max = 5
        j = 0
        while j < 5:
            l = 1
            while l <= l_max and lines[i + 6 - l][j] == '#':
                l += 1
            res_arr.append(l-1)
            j += 1
        #print('key', res_arr)
        key_arr.append(res_arr)
    i += 8

res = 0
for lock in lock_arr:
    for key in key_arr:
        i = 0
        match = True
        while i < 5 and match:
            if lock[i] + key[i] > 5:
                #print(i, lock[i], key[i])
                match = False
            i += 1
        if match:
            res += 1
print(res)
