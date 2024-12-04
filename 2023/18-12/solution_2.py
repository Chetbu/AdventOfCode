# import math
# import copy
# import time



dir = ("U", "R", "D", "L")

dir_matching = ("R", "D", "L", "U")

dir_inc_arr = ((-1,0), (0,1), (1,0), (0,-1))

def next_move(start_coor, move):
    direction = move[0]
    i_dir = dir.index(direction)
    dir_inc = dir_inc_arr[i_dir]


    coor = start_coor

    coor_x = coor[0] + move[1] * dir_inc[0] 
    coor_y = coor[1] + move[1] * dir_inc[1]

    return (coor_x, coor_y)



with open('data.txt') as f:
    lines = f.read().splitlines()

#print(lines)

move_arr = []

for line in lines:
    s = line.split(" ")
    #print(s[2][2:-2])
    hex_num = int(s[2][2:-2],16)
    #print(hex_num)
    #print(dir_matching[int(s[2][-2])])
    move_arr.append((dir_matching[int(s[2][-2])], hex_num))

#print(move_arr)

current_coor = (0,0)
perimeter = 0

edge_coor_array = []

for move in move_arr:
    current_coor = next_move(current_coor, move)
    perimeter += move[1]
    edge_coor_array.append(current_coor)


#print(perimeter)

#print(edge_coor_array)

i = 0
sum_deter = 0
while i < len(edge_coor_array):
    p_0 = edge_coor_array[i-1]
    p_1 = edge_coor_array[i]
    deter = (p_0[0] * p_1[1]) - (p_0[1] * p_1[0])
    #print(p_0, p_1, deter)
    sum_deter += deter
    i += 1


print(abs(sum_deter)/2 + perimeter/2 + 1)









