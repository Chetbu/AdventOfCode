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

def hash_algo_label(s:str):
    #print(s[:2])
    if s[-1] == "-":
        return hash_algo(s[:-1])
    elif s[-2] == "=":
        return hash_algo(s[:-2])
    else:
        print("Error Hash label")

def remove_lense(s:str, box_arr):
    i_box = hash_algo_label(s)
    i = 0
    while i < len(box_arr[i_box]):
        if box_arr[i_box][i][:2] == s[:2]:
            #remove
            del box_arr[i_box][i]
            break
        i += 1
    return box_arr

def add_lense(s:str, box_arr):
    i_box = hash_algo_label(s)
    focal_l = s[-1]

    lense = s[:2] + " " + focal_l
    replaced = False
    i = 0
    while i < len(box_arr[i_box]) and not replaced:
        if box_arr[i_box][i][:2] == s[:2]:
            #replace
            replaced = True
            box_arr[i_box][i] = lense
        i += 1
    
    if not replaced:
        box_arr[i_box].append(lense)

    return box_arr

def focus_power_box(box):
    i = 0
    p = 0
    while i < len(box):
        p += (i+1)*int(box[i][-1])
        i += 1
    return p

def focus_power_box_arr(box_arr):
    i = 0
    p = 0
    while i < len(box_arr):
        p += focus_power_box(box_arr[i]) * (i+1)
        i += 1
    return p



with open('data.txt') as f:
    lines = f.read().splitlines()

s_arr = lines[0].split(',')

i = 0
box_arr = []
while i < 256:
    box_arr.append([])
    i += 1

#print(box_arr)

for s in s_arr:


    if s[-1] == "-":
        box_arr = remove_lense(s, box_arr)
    elif s[-2] == "=":
        box_arr = add_lense(s, box_arr)
    else:
        print("error")
    #print(box_arr[:4])
    
print(focus_power_box_arr(box_arr))

