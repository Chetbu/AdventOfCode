import math
# import copy
import time
import numpy as np

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

def calc_position(robot, sec, width, tallness):
    new_x = robot[0][0] + robot[1][0] * sec
    new_y = robot[0][1] + robot[1][1] * sec
    return (new_x % width, new_y % tallness)

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)
robot_arr = []
for line in lines:
    first_s = line.split(' ')
    pos_arr = first_s[0].split('=')[1].split(',')
    position = (int(pos_arr[0]), int(pos_arr[1]))

    v_arr = first_s[1].split('=')[1].split(',')
    velocity = (int(v_arr[0]), int(v_arr[1]))
    #print(position, velocity)
    robot_arr.append((position, velocity))

#print(robot_arr)

width = 101
tallness = 103

i = 0
i_f = 0
i_max = 10000
var = 1000000
while i < i_max:
    pos_arr = []
    for r in robot_arr:
        pos_arr.append(calc_position(r,i,width,tallness))
    if np.var(pos_arr) < var:
        var = np.var(pos_arr)
        i_f = i
    i += 1

print(var, i_f)