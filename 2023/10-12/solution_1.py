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
print(start)
print(start_dir)

current_coor_dir = [start, start_dir]
current_coor_dir = new_coor_dir(current_coor_dir)
num_step = 1

while current_coor_dir[0] != start:
    current_coor_dir = new_coor_dir(current_coor_dir)
    print(current_coor_dir)
    num_step = num_step + 1

print(num_step / 2)










    








    






 