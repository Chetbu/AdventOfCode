# import math
# import copy
import time

dir_inc_arr = ((-1,0), (0,1), (1,0), (0,-1))

def possible_moves(coor_t: tuple, map_d: dict , dir_inc_t : tuple):
    res = []
    for dir_inc in dir_inc_t:
        new_coor = (
            coor_t[0] + dir_inc[0],
            coor_t[1] + dir_inc[1]
        )
        
        tile_v = map_d[new_coor]
        if tile_v != "#":
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
possible_moves_dict[end_coor] = [(len(lines) - 2, len(lines[0]) - 2)]

raw_intersection_dict = dict()
raw_intersection_dict[start_coor] = [(1,1)]
raw_intersection_dict[end_coor] = [(len(lines) - 2, len(lines[0]) - 2)]
i = 1
while i < len(lines)-1:
    j = 1
    while j < len(lines[0])-1:
        if map_dict[(i,j)] != "#":
            temp = possible_moves((i,j), map_dict, dir_inc_arr)
            possible_moves_dict[(i,j)] = temp
            if len(temp) > 2:
                raw_intersection_dict[(i,j)] = temp
        j += 1
    i += 1

#print(len(raw_intersection_dict))

intersection_distance_dict = dict()

#for each intersection, we go to the next intersection
for c in raw_intersection_dict:
    init = (c, (c,))
    tracer_arr = [init]

    while len(tracer_arr) > 0:
        tracer = tracer_arr.pop(0)
        past_trace = tracer[1]
        possible_c_arr = possible_moves_dict[tracer[0]]
        for p_coor in possible_c_arr:
            if p_coor in raw_intersection_dict and p_coor != c:
                #print(c, p_coor, past_trace)
                intersection_distance_dict[c, p_coor] = len(past_trace)


            elif not p_coor in past_trace:
                new_tracer = (
                    p_coor,
                    past_trace + (p_coor, )
                )
                tracer_arr.insert(0, new_tracer)
        i += 1


    
#print(intersection_distance_dict)

init = (start_coor, (start_coor, ), 0)
tracer_arr = [init]
possible_path_arr = []
possible_l = []
i = 0

max_l = 0

start_time = time.time()
split_time = time.time()


while len(tracer_arr) > 0:
    tracer = tracer_arr.pop(0)
    past_trace = tracer[1]
    possible_c_arr = [x[1] for x in list(intersection_distance_dict) if x[0] == tracer[0]]
    #print(possible_c_arr)
    for p_coor in possible_c_arr:
        add_l = intersection_distance_dict[(tracer[0], p_coor)]
        if p_coor == end_coor:
            possible_path_arr.append(past_trace + (p_coor, ))
            possible_l.append(tracer[2] + add_l)

        elif not p_coor in past_trace:
            new_tracer = (
                p_coor,
                past_trace + (p_coor, ),
                tracer[2] + add_l
            )
            tracer_arr.insert(0, new_tracer)
    i += 1
    if i % 100000 == 0:
        print(i, len(tracer_arr), tracer_arr[0][1][-1], max(possible_l), time.time() - split_time, time.time() - start_time)
        split_time = time.time()

print(possible_path_arr)
print(max(possible_l))





