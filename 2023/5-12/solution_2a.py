# import math
# import copy
import time

#import operator

def arr_eval(arr):
    return arr.split(" ")

with open('data.txt') as f:
    lines = f.read().splitlines()
    #lines_array = list(map(arr_eval,lines))

#print(lines)


name_arr = [
    'seed-to-soil map:',
    'soil-to-fertilizer map:',
    'fertilizer-to-water map:',
    'water-to-light map:',
    'light-to-temperature map:',
    'temperature-to-humidity map:',
    'humidity-to-location map:'
]

maps_array = []
for name in name_arr:
    i = lines.index(name)

    j = i + 1
    while lines[j] != '':
        j = j + 1
        if j == len(lines):
            break
    #print(lines[i+1:j])
    map_temp_arr = []
    for coord_map in lines[i+1:j]:
        temp_arr = coord_map.split(" ")
        c_arr = []
        for t in temp_arr:
            c_arr.append(int(t))
        map_temp_arr.append(c_arr)
    maps_array.append(map_temp_arr)
#print(len(maps_array))

seed_arr = []
seed_arr_range = []
for seed_str in lines[0].split(" ")[1:]:
    seed_arr_range.append(int(seed_str))


def next_range(start_range, iteration:int):
    coor = maps_array[iteration]
    new_start_coor = start_range[0]
    new_end_coor = start_range[1]
    for c in coor:
        if c[1]<= start_range[0] < c[1] + c[2]:
            new_start_coor = c[0] + start_range[0] - c[1]
            new_end_coor = min(
                new_start_coor + start_range[1] - start_range[0],
                c[1] + c[2] -1 - start_range[0] + new_start_coor
                )
            #print(iteration, end_coor)
    if new_start_coor == start_range[0]:
        for c in coor:
            if c[1] > start_range[0]:
                new_end_coor = min(new_end_coor, c[1] - 1)
    return [new_start_coor,new_end_coor]

#print(next_coor(13,0))

res = 1000000000000000000000
start = time.time()

#seed_arr_range = [79,7]

i = 0
while i < len(seed_arr_range):
    full_range = [seed_arr_range[i],seed_arr_range[i]+seed_arr_range[i+1] - 1]

    studied_range = [seed_arr_range[i],seed_arr_range[i]+seed_arr_range[i+1] - 1]

    l = 0

    continue_loop = True
    ite=0
    while continue_loop:
        ite = ite + 1
        #print(studied_range)
        for iteration in range(len(maps_array)):
            studied_range = next_range(studied_range,iteration)
            #print(studied_range)
        
        res = min(res, studied_range[0])
        print("range ", [full_range[0] + l, full_range[0] + l + studied_range[1] -studied_range[0]], "becomes range", studied_range)
        


        if full_range[0] + l + studied_range[1] -studied_range[0] == full_range[1]:
            continue_loop = False
        else:
            l = l + studied_range[1] -studied_range[0] + 1
            studied_range = [full_range[0] + l, full_range[1]]

            print("new iteration on" , studied_range)

    i = i + 2
    print("one done", time.time()-start)


print(res)




    






 