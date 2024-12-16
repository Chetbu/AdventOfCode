import math
# import copy
import time

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
target_time = 100

pos_arr = []
for r in robot_arr:
    pos_arr.append(calc_position(r,target_time,width,tallness))

# pos_arr.sort()
# print(pos_arr)

mid_width = (width-1)/2
mid_tallness = (tallness-1)/2

#count quadrant
quadrant_count = [0,0,0,0]
center_count = 0
for r in pos_arr:
    if r[0] == mid_width or r[1] == mid_tallness:
        center_count += 1
    elif r[0] < mid_width:
        if r[1] < mid_tallness:
            quadrant_count[0] += 1
        else:
            quadrant_count[1] += 1
    else:
        if r[1] < mid_tallness:
            quadrant_count[2] += 1
        else:
            quadrant_count[3] += 1
#print(quadrant_count, center_count)
print(quadrant_count[0] * quadrant_count[1] * quadrant_count[2] * quadrant_count[3])