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


    
def next_coor(start_coor:int, iteration:int):
    coor = maps_array[iteration]
    end_coor = start_coor
    for c in coor:
        if c[1]<= start_coor < c[1] + c[2]:
            end_coor = c[0] + start_coor - c[1]
            #print(iteration, end_coor)
    return end_coor

#print(next_coor(13,0))

res = 1000000000000000000000
start = time.time()

i = 0
while i < len(seed_arr_range):
    j = 0
    while j < seed_arr_range[i+1]:
        new_coor = seed_arr_range[i] + j
        for iteration in range(len(maps_array)):
            new_coor = next_coor(new_coor,iteration)
        res = min(res, new_coor)

        j = j + 1
        if j % 100000 == 0:
            print((j / seed_arr_range[i+1])*100)
    
    i = i + 2
    print("one done", time.time()-start)


print(res)




    






 