# import math
# import copy
# import time

dir_inc_arr = ((-1,0), (0,1), (1,0), (0,-1))

def possible_moves(coor_t: tuple, map_d: dict , dir_inc_t : tuple):
    res = []
    for dir_inc in dir_inc_t:
        new_coor = (
            coor_t[0] + dir_inc[0],
            coor_t[1] + dir_inc[1]
        )
        
        tile_v = map_d[new_coor]
        if tile_v == ".":
            res.append(new_coor)
        elif dir_inc == (-1, 0) and  tile_v == "^":
            res.append(new_coor)
        elif dir_inc == (1, 0) and  tile_v == "v":
            res.append(new_coor)
        elif dir_inc == (0, -1) and  tile_v == "<":
            res.append(new_coor)
        elif dir_inc == (0, 1) and  tile_v == ">":
            res.append(new_coor)

    return res




#print(expand_brick(((2, 2, 339), (2, 2, 348))))   

# def brick_fall(coor_c, z_fall, occupied_space_a):

with open('data.txt') as f:
    lines = f.read().splitlines()

#print(lines)

#to change a bit,create a dict where key are coor and value is content of the tile

map_dict = dict()
i = 0
while i < len(lines):
    j = 0
    while j < len(lines[0]):
        map_dict[(i,j)] = lines[i][j]
        j += 1
    i += 1

start_coor = (0,1)
end_coor = (len(lines) - 1, len(lines[0]) - 2)


possible_moves_dict = dict()
possible_moves_dict[start_coor] = [(1,1)]
i = 1
while i < len(lines)-1:
    j = 1
    while j < len(lines[0])-1:
        if map_dict[(i,j)] != "#":
            possible_moves_dict[(i,j)] = possible_moves((i,j), map_dict, dir_inc_arr)
        j += 1
    i += 1


init = (start_coor, (start_coor))
tracer_arr = [init]
possible_path_arr = []
i = 0

max_l = 0

while len(tracer_arr) > 0:
    tracer = tracer_arr.pop(0)
    past_trace = tracer[1]
    possible_c_arr = possible_moves_dict[tracer[0]]
    for p_coor in possible_c_arr:
        if p_coor == end_coor:
            possible_path_arr.append(past_trace + (p_coor, ))
            max_l = len(past_trace) -1

        elif not p_coor in past_trace:
            new_tracer = (
                p_coor,
                past_trace + (p_coor, )
            )
            tracer_arr.append(new_tracer)
    i += 1
    if i % 100 == 0:
        print(i, len(tracer_arr))

#print(possible_path_arr)
print(max_l)



