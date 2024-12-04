# import math
# import copy
import time
from functools import lru_cache

#import operator

@lru_cache
def source_detected(row,instruct):
    expected_num_source = instruct[0]
    #check if it is possible
    if len(row) < expected_num_source:
        return 0
    elif "." in row[:expected_num_source]:
        #impossible case
        return 0
    else:
        #adding a . at the end to deal with edge cases
        r = row + "." 
        if r[expected_num_source ] == "#":
            #impossible
            return 0
        else:
            return calc_possibilities(r[expected_num_source + 1:],tuple(list(instruct)[1:]))

@lru_cache
def calc_possibilities(row, instruct):
    #print(row, instruct)

    if len(instruct) == 0:
        #if no more expected sources
        if "#" in row:
            #impossible, need to close the case
            return 0
        else:
            #is possible
            #print("possible")
            return 1
    elif len(row) == 0:
        #row is finished but instruction are not, case is not successful
        return 0
    else:
        #we are still expecting at least a source in the rest of the row
        next_char = row[0]

        if next_char == ".":
            #nothing happends, we study the same thing but with one less char
            return calc_possibilities(row[1:], instruct)
        
        elif next_char == "#":
            return source_detected(row,instruct)
        
        else:
            return calc_possibilities(row[1:], instruct) + source_detected(row,instruct)


with open('data.txt') as f:
    lines = f.read().splitlines()


line_array = []
for line in lines:
    l = line.split(" ")
    l_nbr = l[1].split(",")

    row = l[0]

    # row = l[0].replace(".","0")
    # row = row.replace("#","1")

    arr = []
    for n in l_nbr:
        arr.append(int(n))

    line_array.append(
        (row, tuple(arr))
    )
#print(line_array)

ex_line_array = []
for l in line_array:
    arr = list(l[1])
    row = l[0] + "?" + l[0] + "?" + l[0] + "?" + l[0] + "?" + l[0]
    eval = tuple(arr + arr + arr + arr + arr)
    ex_line_array.append(
        (row, eval)
    )

start_time = time.time()

#line_array = [line_array[5]]

res = 0
for line in ex_line_array:
    count = calc_possibilities(line[0], line[1])
    

    
    print(count)
    res += count

print(res, time.time() - start_time)






 