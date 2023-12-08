# import math
# import copy
import time
import json
import pickle

cardinal_arr = (
    ("N", (-1,0)),
    ("S", (1,0)),
    ("W", (0,-1)),
    ("E", (0,1))
)

def extract_coor(b:tuple):
    return b[1]

def next_position(b:tuple, m_size:tuple):
    i = 0
    while cardinal_arr[i][0] != b[0]:
        i += 1
    
    temp_coor_x = b[1][0] + cardinal_arr[i][1][0]
    temp_coor_y = b[1][1] + cardinal_arr[i][1][1]
    

    if temp_coor_x == 0:
        temp_coor_x = m_size[0] - 1
    elif temp_coor_x == m_size[0]:
        temp_coor_x = 1

    if temp_coor_y == 0:
        temp_coor_y = m_size[1] - 1
    elif temp_coor_y == m_size[1]:
        temp_coor_y = 1
    
    return (b[0],(temp_coor_x, temp_coor_y))


with open('data.txt') as f:
    lines = f.read().splitlines()

#print(lines)

#blizzard are direction (N/E/S/W) + coord

b_arr = []
map_limit_index = (len(lines) - 1, len(lines[0]) - 1)
#print(map_limit_index)
i = 1
while i < len(lines) - 1:
    j = 1
    while j < len(lines[0]) - 1:
        if lines[i][j] == ">":
            b_arr.append(("E", (i, j)))
        elif lines[i][j] == "<":
            b_arr.append(("W", (i, j)))
        elif lines[i][j] == "v":
            b_arr.append(("S", (i, j)))
        elif lines[i][j] == "^":
            b_arr.append(("N", (i, j)))
        j +=1
    i+=1

# state 0 is calculated
b_state_arr = [tuple(b_arr)]

st = time.time()
i = 0
state_arr = []
while tuple(state_arr) != b_state_arr[0]:
    state_arr = []
    for el in b_state_arr[i]:
        state_arr.append(next_position(el, map_limit_index))
    b_state_arr.append(tuple(state_arr))
    i += 1

del b_state_arr[-1]
b_state_t = tuple(b_state_arr)
print("States of blizzards solved, time ", time.time() - st)

st = time.time()
time_space_arr = []
for b_s in b_state_t:
    space_arr = [(0,1),(map_limit_index[0],map_limit_index[1]-1)]
    i = 1
    coor_arr=list(map(extract_coor,b_s))
    #print(coor_arr)
    while i < map_limit_index[0]:
        j = 1
        while j < map_limit_index[1]:
            if not((i, j) in coor_arr):
                space_arr.append((i,j))
            j += 1
        i += 1
    #print(space_arr)
    time_space_arr.append(tuple(space_arr))

print("empty space solved, time ", time.time() - st)

# with open('output_test.txt', 'w') as filehandle:
#     json.dump(time_space_arr, filehandle)

with open('data_output.pickle', 'wb') as filehandle:
    pickle.dump(tuple(time_space_arr), filehandle)

# with open('data_test.pickle', 'rb') as f:
#      test_d = pickle.load(f)
#      print(test_d)










    






 