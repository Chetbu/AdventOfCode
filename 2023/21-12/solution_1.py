# import math
# import copy
# import time

dir_inc_arr_t = ((-1,0), (0,1), (1,0), (0,-1))

def possible_move(coor, map, dir_inc_t):
    res = []
    for dir_inc in dir_inc_t:
        #print(coor, dir_inc)
        new_coor = (coor[0] + dir_inc[0], coor[1] + dir_inc[1])
        if 0 <= new_coor[0] < len(map) and 0 <= new_coor[1] < len(map[0]):
            new_tile = map[new_coor[0]][new_coor[1]]
            if new_tile != "#":
                res.append(new_coor)

    return res

    



with open('data.txt') as f:
    lines = f.read().splitlines()

#print(lines)

#find the start

i = 0
while i < len(lines):
    if "S" in lines[i]:
        start_coor = (i, lines[i].index("S"))
        break
    i = i + 1

print(start_coor)

coor_arr = (start_coor, )
i = 0
i_limit = 64
while i < i_limit:
    new_coor_arr = []
    for c in coor_arr:
        new_coor_arr = new_coor_arr + possible_move(c,lines,dir_inc_arr_t)
    coor_arr = tuple(dict.fromkeys(new_coor_arr))
    #print(coor_arr)
    i += 1
    print(i)

print(len(coor_arr))




