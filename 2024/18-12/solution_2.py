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
    (0,-1),
    (1,0),
    (-1,0)
)

def solveable_maze(dir_arr, maze_d):
    result_d = {}
    move_to_do = [((0,0), 0)]
    count = 0
    while len(move_to_do) > 0:
        current_pos_score_t = move_to_do.pop(0)
        temp = move(current_pos_score_t, dir_arr, result_d, maze_d)
        move_to_do += temp[0]
        result_d = temp[1]
        count += 1
        if count % 10000 == 0:
            print(len(move_to_do))

    return (max_d, max_d) in result_d
    #print(result_d[(max_d, max_d)])

def move(pos_score_t:tuple, dir_arr:list, result_d:dict, maze_d:dict):
    #generate the possible moves and put the results in the result dict
    pos = pos_score_t[0]
    score = pos_score_t[1]
    res = []
    for dir in dir_arr:
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if new_pos in maze_d and maze_d[new_pos] != '#':
            #move is possible
            if new_pos in result_d:
                if result_d[new_pos][1] > score + 1:
                    result_d[new_pos] = (new_pos, score + 1)
                    res.append((new_pos, score + 1))
            else:
                result_d[new_pos] = (new_pos, score + 1)
                res.append((new_pos, score + 1))
    return (res, result_d)

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)
b_arr = []

for line in lines:
    s = line.split(',')
    b_arr.append((int(s[0]), int(s[1])))

#print(b_arr)

#create the empty maze
maze_d = {}
max_d = 70
i = 0
while i <= max_d:
    j = 0
    while j <= max_d:
        maze_d[(i,j)] = '.'
        j += 1
    i += 1
#make the bytes fall

i = 0
solveable = True
while i < len(b_arr) and solveable:
    maze_d[b_arr[i]] = '#'
    solveable = False
    if solveable_maze(dir_arr, maze_d):
        i += 1
        solveable = True

print(str(b_arr[i][0])+','+str(b_arr[i][1]), i, time.time() - start_time)
