import math
# import copy
import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

move_dict = {
    '^' : (-1,0),
    '<' : (0,-1),
    '>' : (0,1),
    'v' : (1,0)
}

def calc_new_coord(coor, move_s):
    m = move_dict[move_s]
    return (coor[0] + m[0], coor[1] + m [1])

def eval_maze(coor, maze):
    return maze[coor]

def calc_move_collision(coor, move_s, maze):
    new_coor = calc_new_coord(coor, move_s)
    if eval_maze(new_coor, maze) == '.':
        # space is empty, continue
        maze[coor] = '.'
        maze[new_coor] = '@'
        return (new_coor, maze)
    elif eval_maze(new_coor, maze) == '#':
        #wall, does not move
        return (coor, maze)
    else:
        #box is detected
        i = 1
        box_coor = new_coor
        while eval_maze(box_coor, maze) == 'O':
            i += 1
            box_coor = calc_new_coord(box_coor, move_s)
        if eval_maze(box_coor, maze) == '.':
            #all the box moves, along the robot
            maze[coor] = '.'
            maze[new_coor] = '@'
            maze[box_coor] = 'O'
            return (new_coor, maze)
        else:
            #no move
            return (coor, maze)


with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

i_split = lines.index('')
maze_arr = lines[:i_split]
instructions = lines[i_split + 1:]

#create the maze_dict with coor and find the robot
maze_dict = {}
i = 0
pos = (-1,-1)
while i < len(maze_arr):
    j = 0
    while j < len(maze_arr[i]):
        maze_dict[(i,j)] = maze_arr[i][j]
        if maze_arr[i][j] == '@':
            pos = (i,j)

        j += 1
    i += 1
print(pos)

for line in instructions:
    for s in line:
        move = calc_move_collision(pos, s, maze_dict)
        pos = move[0]
        maze_dict = move[1]

#map all the boxes
i = 0
box_gps_coor = 0
while i < len(maze_arr):
    j = 0
    while j < len(maze_arr[i]):
        if maze_dict[(i,j)] == 'O':
            box_gps_coor += 100 * i + j
        j += 1
    i += 1

print(box_gps_coor)