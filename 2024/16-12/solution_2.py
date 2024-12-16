import math
# import copy
import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

dir_arr = (
    (0,1),
    (1,0),
    (0,-1),
    (-1,0)
)

def cal_possible_moves(pos_dir_score_t, maze, dir_arr):
    pos = pos_dir_score_t[0]
    #go forward
    res = []
    pos_forward = (pos[0] + dir_arr[pos_dir_score_t[1]][0], pos[1] + dir_arr[pos_dir_score_t[1]][1])
    if maze[pos_forward] != '#':
        res.append((pos_forward, pos_dir_score_t[1], pos_dir_score_t[2] + 1))
    #rotate
    res += [
        (pos, (pos_dir_score_t[1] + 1) % 4, pos_dir_score_t[2] + 1000),
        (pos, (pos_dir_score_t[1] + 3) % 4, pos_dir_score_t[2] + 1000)
    ]
    return res

def cal_backtrack_possible_moves(pos_dir_score_t, maze, dir_arr):
    pos = pos_dir_score_t[0]
    #go forward
    res = []
    pos_backward = (pos[0] - dir_arr[pos_dir_score_t[1]][0], pos[1] - dir_arr[pos_dir_score_t[1]][1])

    res.append((pos_backward, pos_dir_score_t[1], pos_dir_score_t[2] - 1))
    #rotate
    res += [
        (pos, (pos_dir_score_t[1] + 1) % 4, pos_dir_score_t[2] - 1000),
        (pos, (pos_dir_score_t[1] + 3) % 4, pos_dir_score_t[2] - 1000)
    ]
    return res

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

#create the maze_dict with coor and find the robot
maze_dict = {}
i = 0
pos_start = (-1,-1)
pos_end = (-1,-1)
while i < len(lines):
    j = 0
    while j < len(lines[i]):
        maze_dict[(i,j)] = lines[i][j]
        if lines[i][j] == 'S':
            pos_start = (i,j)
        elif lines[i][j] == 'E':
            pos_end = (i,j)

        j += 1
    i += 1
#print(pos_start, pos_end)

#init
result_dict = {(pos_start, 0) : 0}
pos_to_eval_arr = [(pos_start, 0, 0)]
while len(pos_to_eval_arr) > 0:
    current_t = pos_to_eval_arr.pop(0)
    possible_position_arr = cal_possible_moves(current_t, maze_dict,dir_arr)
    #print(possible_position_arr)
    #add to the result dict the lowest score possible for a given position and orientation
    for ele in possible_position_arr:
        coor_dir = (ele[0], ele[1])
        if not(coor_dir in result_dict):
            result_dict[coor_dir] = ele[-1]
            pos_to_eval_arr.append(ele)
        elif ele[-1] < result_dict[coor_dir]:
            result_dict[coor_dir] = ele[-1]
            pos_to_eval_arr.append(ele)
    #print(pos_to_eval_arr)

i = 0
possible_result = []
while i < 4:
    if (pos_end, i) in result_dict:
        possible_result.append((i, result_dict[(pos_end, i)]))
    i += 1
min_res = min([x[1] for x in possible_result])
index_r = [x[1] for x in possible_result].index(min_res)
end_pos_dir_score_t = (pos_end, possible_result[index_r][0], possible_result[index_r][1])

#print(end_pos_dir_score_t)

#now backtrack to see what are the possible paths to get here
pos_to_eval_arr = [end_pos_dir_score_t]
tile_arr = [pos_end]
while len(pos_to_eval_arr) > 0:
    current_t = pos_to_eval_arr.pop(0)
    possible_position_arr = cal_backtrack_possible_moves(current_t, maze_dict,dir_arr)
    #check if the possible move is in results_dict
    
    for ele in possible_position_arr:
        coor_dir = (ele[0], ele[1])
        if coor_dir in result_dict:
            #print(coor_dir)
            if result_dict[coor_dir] == ele[2]:

                pos_to_eval_arr.append(ele)
                tile_arr.append(ele[0])

print(len(set(tile_arr)))


