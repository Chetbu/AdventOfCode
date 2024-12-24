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

def cal_possible_moves(pos_score_t, maze, dir_arr):
    pos = pos_score_t[0]
    score = pos_score_t[1]
    #go forward
    res = []
    for dir in dir_arr:
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if maze[new_pos] != '#':
            res.append((new_pos, score + 1))
    return res

def gen_cheating_move_arr(pos_score_t, limit):
    pos = pos_score_t[0]
    score = pos_score_t[1]
    x = 0
    res = []
    while x <= limit:
        y = 0
        while x + y <= limit:
            new_pos_score_arr = [
                ((pos[0] + x, pos[1] + y), score + x + y),
                ((pos[0] - x, pos[1] + y), score + x + y),
                ((pos[0] + x, pos[1] - y), score + x + y),
                ((pos[0] - x, pos[1] - y), score + x + y),
            ]
            res += new_pos_score_arr
            y += 1
        x += 1
    return list(set(res))

#print(len(gen_cheating_move_arr(((2,2),0),3)))

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

#create the maze_dict with coor and find the start and end
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
result_dict = {(pos_start) : 0}
pos_to_eval_arr = [(pos_start, 0)]
while len(pos_to_eval_arr) > 0:
    current_t = pos_to_eval_arr.pop(0)
    possible_position_arr = cal_possible_moves(current_t, maze_dict,dir_arr)
    #print(possible_position_arr)
    #add to the result dict the lowest score possible for a given position and orientation
    for ele in possible_position_arr:
        coor_dir = ele[0]
        if not(coor_dir in result_dict):
            result_dict[coor_dir] = ele[-1]
            pos_to_eval_arr.append(ele)
        elif ele[-1] < result_dict[coor_dir]:
            result_dict[coor_dir] = ele[-1]
            pos_to_eval_arr.append(ele)
    #print(pos_to_eval_arr)

normal_time = result_dict[pos_end]
print(normal_time, time.time() - start_time) #expected value in test = 84

#Redo the algo, starting from the end , and try to cheat
pos_to_eval_arr = [(pos_end, 0)]
result_backward_d = {(pos_end) : 0}
list_cheat = []
while len(pos_to_eval_arr) > 0:
    current_t = pos_to_eval_arr.pop(0)
    #try to cheat
    t_max_cheat = 20
    possible_cheat_moves = gen_cheating_move_arr(current_t, t_max_cheat)

    for ele in possible_cheat_moves:

        if ele[0] in result_dict:

            #back on normal track, test if the cheat is good
            potential_l = ele[1] + result_dict[ele[0]]
            #print(ele, potential_l)
            if potential_l < normal_time:
                #print('ping')

                cheat_id = (current_t[0], ele[1])
                list_cheat.append((cheat_id, normal_time - potential_l))

    #do normal diffusion
    possible_position_arr = cal_possible_moves(current_t, maze_dict,dir_arr)
    #print(possible_position_arr)
    #add to the result dict the lowest score possible for a given position and orientation
    for ele in possible_position_arr:
        coor_dir = ele[0]
        if not(coor_dir in result_backward_d):
            result_backward_d[coor_dir] = ele[-1]
            pos_to_eval_arr.append(ele)
        elif ele[-1] < result_backward_d[coor_dir]:
            result_backward_d[coor_dir] = ele[-1]
            pos_to_eval_arr.append(ele)
    #print(pos_to_eval_arr)

#list_cheat = list(set(list_cheat))
count_test = 0
for c in list_cheat:
    if c[1] == 72:
        count_test += 1
print(count_test)

count = 0
for c in list_cheat:
    if c[1] >= 100:
        count += 1
print(count)