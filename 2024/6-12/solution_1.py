# import math
# import copy
# import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

dir_arr = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]

def eval_position(matrix, pos):
    return matrix[pos[0]][pos[1]]

def move(matrix, dir_arr, pos_dir_list):
    #return the next position and dir
    start_pos = pos_dir_list[0]
    dir_index = pos_dir_list[1]

    #test if the next possible square is free
    dir = dir_arr[dir_index]
    next_pos = (start_pos[0] + dir[0], start_pos[1] + dir[1])
    if not(0 <= next_pos[0] < len(matrix)) or not(0 <= next_pos[1] < len(matrix[0])):
        return [start_pos, -1]
    elif eval_position(matrix,next_pos) == "#":
        #turn 90
        new_dir_index = (dir_index + 1) % 4
        return [start_pos, new_dir_index]
        #return move(matrix, dir_arr, [start_pos, new_dir_index])
    else:
        return [next_pos, dir_index]

#find start
start_pos = (0,0)
i = 0
found = False
while i < len(lines) and not(found):
    if lines[i].find("^") >= 0:
        start_pos = (i, lines[i].find("^"))
        found = True
    i += 1

#print(start_pos)

pos_dir_l = [start_pos, 0]
pos_arr = [start_pos]
while pos_dir_l[1] != -1:
    pos_dir_l = move(lines, dir_arr,pos_dir_l)
    pos_arr.append(pos_dir_l[0])

print(len(list(dict.fromkeys(pos_arr))))




