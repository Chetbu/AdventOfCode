# import math
import copy
# import time

#import operator

def arr_eval(arr):
    temp = arr.split(" ")
    res = []
    for item in temp:
        res.append(int(item))
    return res

with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_eval,lines))


#print(lines_array)

def isSafe(eval_arr):
    eval_min = min(eval_arr)
    eval_max = max(eval_arr)

    eval_safe = True
    #Differents signs = False
    if eval_min*eval_max <= 0:
        eval_safe = False
    elif max(- eval_min, eval_max) > 3:
        eval_safe = False
    
    return eval_safe

def create_eval_array(line_array, skip_index):
    j = 1
    eval_arr = []
    line_array_skipped = copy.copy(line_array)
    #print(line_array_skipped)
    del line_array_skipped[skip_index]
    #print(line_array_skipped)
    while j < len(line_array_skipped):
        eval_arr.append(line_array_skipped[j] - line_array_skipped[j - 1])
        j  += 1

    return eval_arr


count = 0

i = 0
while i < len(lines_array):
    j = 0
    safe_found = False
    while j < len(lines_array[i]) and not(safe_found):
        eval_arr_temp = create_eval_array(lines_array[i],j)
        #print(eval_arr_temp)
        if isSafe(eval_arr_temp):
            safe_found = True
        j += 1
    
    if safe_found:
        count += 1
    
    i += 1


    


print(count)




 