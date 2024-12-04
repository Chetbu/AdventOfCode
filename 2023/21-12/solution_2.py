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

    
def possible_move_extended(coor, map, dir_inc_t):
    res = []
    for dir_inc in dir_inc_t:
        #print(coor, dir_inc)
        new_coor = (coor[0] + dir_inc[0], coor[1] + dir_inc[1])
        new_tile = map[new_coor[0] % len(map)][new_coor[1]% len(map[0])]
        if new_tile != "#":
            res.append(new_coor)

    return res


with open('data.txt') as f:
    lines = f.read().splitlines()

print(len(lines[0]))

#find the start

i = 0
while i < len(lines):
    if "S" in lines[i]:
        start_coor = (i, lines[i].index("S"))
        break
    i = i + 1

#print(start_coor)

# print("#" in lines[start_coor[0]])
# print("#" in [x[start_coor[1]] for x in lines])

# no boulders on the line and collumn of the start, meaning that we can go to the edge easily

# calc the number of step to fill a till from the S marker

coor_arr = (start_coor, )
coor_new = (start_coor, )
coor_arr_memory = [coor_arr, coor_arr, coor_arr, coor_arr]

coor_arr65 = []
coor_full_visited_65 = []

coor_full_visited = []

# i = 0
# i_limit = 1000
# while i < i_limit:
#     new_coor_arr = []
#     for c in coor_arr:
#         new_coor_arr = new_coor_arr + possible_move(c,lines, dir_inc_arr_t)
    
#     new_coor_arr.sort()

#     coor_arr = tuple(dict.fromkeys(new_coor_arr))

#     del coor_arr_memory[0]
#     coor_arr_memory.append(coor_arr)
#     #print(coor_arr)
#     i += 1
#     print(i)

#     if i % 131 == 65:
#         print(len(coor_arr))
#         coor_arr65 = coor_arr
#         coor_full_visited_65 = coor_arr + coor_arr_memory[2]

#     if coor_arr_memory[2] == coor_arr_memory[0] and coor_arr_memory[3] == coor_arr_memory[1]:
#         coor_full_visited = coor_arr_memory[2] + coor_arr_memory[1]

#         break

# p_arr = coor_full_visited_65    
# print("65 steps total:", len(p_arr), "65 steps even :", len([x for x in p_arr if (x[0] + x[1]) % 2 == 0]), "65 steps odd :", len([x for x in p_arr if (x[0] + x[1]) % 2 == 1]))
# p_arr = coor_full_visited
# print("full map steps total:", len(p_arr), "full steps even :", len([x for x in p_arr if (x[0] + x[1]) % 2 == 0]), "full steps odd :", len([x for x in p_arr if (x[0] + x[1]) % 2 == 1]))

# 65 steps total: 7530 65 steps even : 3731 65 steps odd : 3799
# full map steps total: 15090 full steps even : 7592 full steps odd : 7498

n= int(26501365/131)
print(n)

odd_full = 7498
even_full = 7592

odd_corner = odd_full - 3799
even_corner = even_full - 3731


res = (n + 1) **2 * odd_full + n * n * even_full - (n + 1) * odd_corner + n * even_corner

print(res)