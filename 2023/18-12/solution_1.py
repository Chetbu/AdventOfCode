# import math
# import copy
# import time



dir = ("U", "R", "D", "L")

dir_inc_arr = ((-1,0), (0,1), (1,0), (0,-1))

def next_move(start_coor, move):
    direction = move[0]
    i_dir = dir.index(direction)
    dir_inc = dir_inc_arr[i_dir]

    i = 0
    res = []
    coor = start_coor
    while i < move[1]:
        coor_x = coor[0] + dir_inc[0] 
        coor_y = coor[1] + dir_inc[1]
        coor = (coor_x, coor_y)
        res.append(coor)
        i +=1
    return res



with open('data.txt') as f:
    lines = f.read().splitlines()

#print(lines)

move_arr = []

for line in lines:
    s = line.split(" ")
    move_arr.append((s[0], int(s[1])))

#print(move_arr)

current_coor = (0,0)
coor_array = [current_coor]

edge_coor_array = []

for move in move_arr:
    new_move_array = next_move(current_coor, move)
    current_coor = new_move_array[-1]
    edge_coor_array.append(current_coor)
    for m in new_move_array:
        if not m in coor_array:
            coor_array.append(m)

print(len((coor_array)))

print(edge_coor_array)

i = 0
sum_deter = 0
while i < len(edge_coor_array):
    p_0 = edge_coor_array[i-1]
    p_1 = edge_coor_array[i]
    deter = (p_0[0] * p_1[1]) - (p_0[1] * p_1[0])
    print(p_0, p_1, deter)
    sum_deter += deter
    i += 1

print(abs(sum_deter)/2)
print(abs(sum_deter)/2 + len(coor_array)/2 + 1)

# #look for min and max for x,y
# x_min = 0
# x_max = 0
# y_min = 0
# y_max = 0
# for m in coor_array:
#     x_min = min(x_min, m[0])
#     x_max = max(x_max, m[0])
#     y_min = min(y_min, m[1])
#     y_max = max(y_max, m[1])

# print(x_min, x_max, y_min, y_max)
# interior_arr = []
# for x in range(x_min, x_max):
#     for y in range(y_min, y_max):
#         #print((x,y))
#         if not (x,y) in coor_array:
#             #filter coor_array
#             nbr_x_up = len([ele for ele in coor_array if ele[0] < x and ele[1] == y])
#             nbr_x_down = len([ele for ele in coor_array if ele[0] > x and ele[1] == y])
#             #print(nbr_x_up, nbr_x_down)
#             nbr_y_up = len([ele for ele in coor_array if ele[1] < y and ele[0] == x])
#             nbr_y_down = len([ele for ele in coor_array if ele[1] > y and ele[0] == x])
#             if not (nbr_x_down == 0 or nbr_y_down == 0 or nbr_x_up == 0 or nbr_y_up == 0):
#                 #print("lol")
#                 interior_arr.append((x,y))

# print(len(interior_arr))
# print(len(interior_arr) + len(coor_array))







