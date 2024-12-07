# import math
# import copy
import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)

# Save timestamp
start_time = time.time()


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

def move(matrix, dir_arr, pos_dir_list, additional_block_coord):
    #return the next position and dir
    start_pos = pos_dir_list[0]
    dir_index = pos_dir_list[1]

    #test if the next possible square is free
    dir = dir_arr[dir_index]
    next_pos = (start_pos[0] + dir[0], start_pos[1] + dir[1])
    if not(0 <= next_pos[0] < len(matrix)) or not(0 <= next_pos[1] < len(matrix[0])):
        return (start_pos, -1)
    elif eval_position(matrix,next_pos) == "#" or next_pos == additional_block_coord:
        #turn 90
        new_dir_index = (dir_index + 1) % 4
        #return [start_pos, new_dir_index]
        return move(matrix, dir_arr, [start_pos, new_dir_index], additional_block_coord)
    else:
        return (next_pos, dir_index)

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

pos_dir_l = (start_pos, 0)

path_arr = [pos_dir_l]

#define the path without new blocks
while pos_dir_l[1] != -1:
    pos_dir_l = move(lines,dir_arr,pos_dir_l, (-1,-1))
    path_arr.append(pos_dir_l)

#print(len(path_arr))

successful_blocks_arr = []

i = 1
while i < len(path_arr):
    new_block_coor = path_arr[i][0]
    past_path = path_arr[:i]
    #print(new_block_coor)
    if not(new_block_coor in [x[0] for x in past_path]):
        #print(new_block_coor)

        #add a block on the path and see if it loops

        pos_dir_l = past_path[-1]
        pos_dir_l = move(lines,dir_arr,pos_dir_l, new_block_coor)
        while pos_dir_l[1] != -1 and not(pos_dir_l in past_path):
            past_path.append(pos_dir_l)
            pos_dir_l = move(lines,dir_arr,pos_dir_l, new_block_coor)
            
        if pos_dir_l[1] != -1:
            #loop detected as the while stops without going offbound
            successful_blocks_arr.append(new_block_coor)
    i += 1
    if i % 100 == 0:
        print(i, time.time() - start_time)

# Save timestamp
end_time = time.time()
print(len(successful_blocks_arr), end_time - start_time)

   




