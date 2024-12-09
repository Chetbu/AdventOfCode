# import math
# import copy
# import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")

def locate_nodes(coor1, coor2, lines):
    dif_coor_x = coor2[0] - coor1[0]
    dif_coor_y = coor2[1] - coor1[1]
    res = []

    coor_plus = (coor2[0] + dif_coor_x, coor2[1] + dif_coor_y)
    while 0 <= coor_plus[0] < len(lines) and 0 <= coor_plus[1] < len(lines[0]):
        res.append(coor_plus)
        coor_plus = (coor_plus[0] + dif_coor_x, coor_plus[1] + dif_coor_y)
    coor_moins = (coor1[0] - dif_coor_x, coor1[1] - dif_coor_y)
    while 0 <= coor_moins[0] < len(lines) and 0 <= coor_moins[1] < len(lines[0]):
        res.append(coor_moins)
        coor_moins = (coor_moins[0] - dif_coor_x, coor_moins[1] - dif_coor_y)
    return res

#print(locate_nodes((3,4),(5,3)))

with open(file_filepath) as f:
    lines = f.read().splitlines()

#locate all the nodes for each possible antennas
antenna_loc_arr = {}

i = 0
while i < len(lines):
    j = 0
    while j < len(lines[i]):
        if lines[i][j] != '.':
            if lines[i][j] in antenna_loc_arr:
                antenna_loc_arr[lines[i][j]].append((i,j))
            else:
                antenna_loc_arr[lines[i][j]] = [(i,j)]

        j += 1
    i += 1

#print(antenna_loc_arr)
total_nodes = []

for key in antenna_loc_arr:
    location_arr = antenna_loc_arr[key]
    #print(location_arr)
    i = 0
    node_arr = []
    while i < len(location_arr) - 1:
        j = i + 1
        while j < len(location_arr):
            node_arr += locate_nodes(location_arr[i], location_arr[j],lines)
            j += 1

        i += 1
    #print(node_arr)
    total_nodes += node_arr
    total_nodes += location_arr

dedup_list = list(dict.fromkeys(total_nodes))
#print(dedup_list)
print(len(dedup_list))

