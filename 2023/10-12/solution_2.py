# import math
# import copy
# import time

#import operator

connectors = ["|", "-", "L", "J", "7", "F","S"]
dir = ["N", "E", "S", "W"]

dir_inc_arr = [(-1,0), (0,1), (1,0), (0,-1)]

next_dir_arr = [
    ["N", -1, -1, -1, "W",  "E", "N"],
    [-1, "E", -1, "N", "S", -1, "E"],
    ["S", -1, "E", "W", -1,  -1, "S"],
    [-1, "W", "N", -1, -1, "S", "W"],

]

turn_arr = [
    [-1, -1, -1, -1, "L",  "R", "N"],
    [-1, -1, -1, "L", "R", -1, "E"],
    [-1, -1, "L", "R", -1,  -1, "S"],
    [-1, -1, "R", -1, -1, "L", "W"],

]

left_offset = [(0,-1), (-1,0), (0,1), (1,0)] #in order for N E S W
right_offset = [(0,1), (1,0), (0,-1), (-1,0)] #in order for N E S W

def new_coor_dir(current_coor_dir):
    coor = current_coor_dir[0]
    current_connector = lines[coor[0]][coor[1]]
    i_connector = connectors.index(current_connector)
    i_direction = dir.index(current_coor_dir[1])

    next_dir = next_dir_arr[i_direction][i_connector]
    dir_inc = dir_inc_arr[dir.index(next_dir)]
    next_coor = (
        coor[0] + dir_inc[0],
        coor[1] + dir_inc[1]
    )

    return (next_coor, next_dir)

def possible_offset(current_coor_dir, side):
    res_arr = []
    
    coor = current_coor_dir[0]
    current_connector = lines[coor[0]][coor[1]]
    i_connector = connectors.index(current_connector)
    i_direction = dir.index(current_coor_dir[1])

    if side == "L":
        offset = left_offset
    else:
        offset = right_offset
    coor_offset = offset[i_direction]
    new_coor = (
        coor[0] + coor_offset[0],
        coor[1] + coor_offset[1]
    )
    res_arr.append(new_coor)
    
    turn = turn_arr[i_direction][i_connector]
    #print(current_coor_dir, turn)
    if not current_connector in ["|", "-", "S"] and turn != side:
        dir_inc = dir_inc_arr[dir.index(current_coor_dir[1])]
        new_coor_offset = (
            new_coor[0] + dir_inc[0],
            new_coor[1] + dir_inc[1]
        )
        next_coor = (
            coor[0] + dir_inc[0],
            coor[1] + dir_inc[1]
        )
        res_arr.append(new_coor_offset)
        res_arr.append(next_coor)
    #print(current_coor_dir, turn, res_arr)
    return res_arr


with open('data.txt') as f:
    lines = f.read().splitlines()

#print(lines)
start_dir = "N"
for i in range(len(lines)):
    if lines[i].find("S") > 0:
        j = lines[i].find("S")
        start = (i, j)
        if lines[i][j + 1] in ["-", "J", "7"]:
            start_dir = "E"
        elif lines[i][j - 1] in ["-", "F", "L"]:
            start_dir = "W"

        break
#print(start)
#print(start_dir)

current_coor_dir = (start, start_dir)
steps = 0
path_dir = [current_coor_dir]
path = [start, current_coor_dir[0]]

left_path_node = []
right_path_node = []
left_right_turns = [0,0]
while current_coor_dir[0] != start or steps == 0:
    current_connector = lines[current_coor_dir[0][0]][current_coor_dir[0][1]]
    if not current_connector in ["|", "-"]:
        #Map the direction of the turn to understand the rotation of the loop
        i_direction = dir.index(current_coor_dir[1])
        i_connector = connectors.index(current_connector)
        turn = turn_arr[i_direction][i_connector]
        if turn == "L":
            left_right_turns[0] = left_right_turns[0] + 1
        elif turn == "R":
            left_right_turns[1] = left_right_turns[1] + 1


    path_dir.append(current_coor_dir)
    path.append(current_coor_dir[0])

    left_path_node += possible_offset(current_coor_dir, "L")
    right_path_node += possible_offset(current_coor_dir, "R")


    #print(current_connector)

    current_coor_dir = new_coor_dir(current_coor_dir)
    steps += 1

print(left_right_turns)

left_path_node = list(dict.fromkeys(left_path_node))
right_path_node = list(dict.fromkeys(right_path_node))

for c in path:
    if c in left_path_node:
        left_path_node.remove(c)
    if c in right_path_node:
        right_path_node.remove(c)

#print(left_path_node)
#print(right_path_node)

if left_right_turns[0] > left_right_turns[1]:
    seed_node_array = left_path_node
else:
    seed_node_array = right_path_node

print(seed_node_array)

i = 0
while i < len(seed_node_array):
    coor = seed_node_array[i]
    for coor_offset in left_offset:
        new_coor = (
            coor[0] + coor_offset[0],
            coor[1] + coor_offset[1]
        )
        if not (new_coor in path) and not (new_coor in seed_node_array):
            seed_node_array.append(new_coor)
    i = i + 1
    if i % 100 == 0:
        print(i, len(seed_node_array))

print((seed_node_array))
print(len(seed_node_array))      

    













    








    






 