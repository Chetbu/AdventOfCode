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

def bitwise_XOR(a,b):
    #XOR on the number
    f_b = bin(max(a,b))
    s_b = bin(min(a,b))

    #print(f_b, s_b)
    i = -1
    res_b = ""
    while s_b[i] != 'b':
        if f_b[i] != s_b[i] and int(f_b[i]) + int(s_b[i]) == 1:
            res_b = '1' + res_b
        else:
            res_b = '0' + res_b
        i -= 1
    #print(f_b[:i+1])
    res_b = f_b[:i+1] + res_b
    return int(res_b, 2)

#print(bitwise_XOR(42,15))

def prune(n):
    return n % 16777216

#print(prune(100000000))
def calc_next_secret(n):
    secret = n
    first_step = prune(bitwise_XOR(secret * 64, secret))
    secret = first_step
    second_step = prune(bitwise_XOR(int(secret/ 32), secret))
    secret = second_step
    third_step = prune(bitwise_XOR(secret * 2048, secret))
    return third_step

#print(calc_next_secret(123))     

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

count = 0
for s in [int(x) for x in lines]:
    i = 0
    res_loop = s
    while i < 2000:
        res_loop = calc_next_secret(res_loop)

        i += 1
    #print(res_loop)
    count += res_loop

print(count)