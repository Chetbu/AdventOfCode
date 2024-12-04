# import math
# import copy
# import time

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
for seed_str in lines[0].split(" ")[1:]:
    seed_arr.append(int(seed_str))
#print(seed_arr)


    
def next_coor(start_coor:int, iteration:int):
    coor = maps_array[iteration]
    end_coor = start_coor
    for c in coor:
        if c[1]<= start_coor < c[1] + c[2]:
            end_coor = c[0] + start_coor - c[1]
    return end_coor

#print(next_coor(13,0))

res_array = []
for seed in seed_arr:
    new_coor = seed
    res_seed = [seed]
    for i in range(len(maps_array)):
        new_coor = next_coor(new_coor,i)
        res_seed.append(new_coor)
    res_array.append(res_seed)

res = res_array[0][7]
for r in res_array:
    res = min(res,r[7])

print(res)




    






 