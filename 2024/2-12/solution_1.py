# import math
# import copy
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

count = 0

i = 0
while i < len(lines_array):
    j = 1
    eval_arr = []
    while j < len(lines_array[i]):
        eval_arr.append(lines_array[i][j] - lines_array[i][j - 1])
        j  += 1

    eval_min = min(eval_arr)
    eval_max = max(eval_arr)

    eval_safe = True
    #Differents signs = False
    if eval_min*eval_max <= 0:
        eval_safe = False
    elif max(- eval_min, eval_max) > 3:
        eval_safe = False
    
    #print(eval_min, eval_max, eval_safe)

    if eval_safe:
        count += 1

    i += 1

print(count)




 