# import math
# import copy
# import time

def next_value(v, char):
    ascii_value = ord(char)
    new_v = 17 * (ascii_value + v)
    return new_v % 256

def hash_algo(s:str):
    i = 0
    v = 0
    while i < len(s):
        v = next_value(v, s[i])
        i += 1
    return v



# print(next_value(0,"H"))
# print(next_value(200,"A"))
#print(hash_algo("HASH"))


with open('data.txt') as f:
    lines = f.read().splitlines()

s_arr = lines[0].split(',')

res = 0
for s in s_arr:
    res += hash_algo(s)

# print(s_arr)
print(res)

