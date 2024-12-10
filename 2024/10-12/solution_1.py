# import math
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

def next_step(position_t, lookup_value, dir_arr, matrix):
    res = []
    # if lookup_value == 9:
    #     return [position_t]
    for dir in dir_arr:
        new_position = (position_t[0] + dir[0], position_t[1] + dir[1])
        if 0 <= new_position[0] < len(matrix) and 0 <= new_position[1] < len(matrix[0]):
            if int(matrix[new_position[0]][new_position[1]]) == lookup_value:
                if lookup_value == 9:
                    res.append(new_position)
                else:
                    res = res + next_step(new_position, lookup_value + 1, dir_arr, matrix)
    return res


with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

#run in the data and find 0
i = 0
total_score = 0
while i < len(lines):
    j = 0
    while j < len(lines[i]):
        if lines[i][j] == '0':
            #print(next_step((i,j), 1, dir_arr, lines))
            
            dedup_list = list(dict.fromkeys(next_step((i,j), 1, dir_arr, lines)))
            total_score += len(dedup_list)
        j += 1
    i += 1
print(total_score)