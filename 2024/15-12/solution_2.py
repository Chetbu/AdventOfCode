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

def generate_box_coor(coor_detec, maze):
    if eval_maze(coor_detec, maze) == "[":
        return (coor_detec, calc_new_coord(coor_detec, '>'))
    else:
        return (calc_new_coord(coor_detec, '<'), coor_detec)


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
        #box is detected, map the array of boxes
        #print('Box detected')

        box_coor_arr = []
        
        if move_s in ['<', '>']:
            #print("box horizontal")
            #move horizontal
            box_coor = new_coor
            while eval_maze(box_coor, maze) in ['[',']']:
                box_coor_arr.append(generate_box_coor(box_coor, maze))
                box_coor = calc_new_coord(calc_new_coord(box_coor, move_s),move_s)
            if eval_maze(box_coor,maze) == '#':
                #no move
                return (coor, maze)
            else:
                #move the robot and the boxes
                maze[coor] = '.'
                maze[new_coor] = '@'
                for b in box_coor_arr:
                    maze[calc_new_coord(b[0], move_s)] = '['
                    maze[calc_new_coord(b[1], move_s)] = ']'
                return (new_coor, maze)
        else:
            #move vertical, more tricky
            box_coor = generate_box_coor(new_coor, maze)
            #populate the box array of all the box touching the previous box in the array
            box_coor_arr = [box_coor]
            
            i = 0
            wall_detected = False
            while i < len(box_coor_arr) and not(wall_detected):
                current_box = box_coor_arr[i]
                for c in current_box:
                    new_coor_c = calc_new_coord(c, move_s)
                    if eval_maze(new_coor_c, maze) == '#':
                        #wall detected, no move possible
                        wall_detected = True
                    elif eval_maze(new_coor_c, maze) in ['[',']']:
                        new_box_coor_t = generate_box_coor(new_coor_c, maze)
                        if not(new_box_coor_t in box_coor_arr):
                            box_coor_arr.append(new_box_coor_t)
                i += 1
                
            
            if wall_detected:
                #no move, as a wall was detected blocking a box in the array
                return (coor, maze)
            else:
                #every box can be push as there is a empty wall behind, switching all the coordinates
                #erase the boxes first
                for b in box_coor_arr:
                    maze[b[0]] = '.'
                    maze[b[1]] = '.'
                maze[coor] = '.'
                maze[new_coor] = '@'
                for b in box_coor_arr:
                    maze[calc_new_coord(b[0], move_s)] = '['
                    maze[calc_new_coord(b[1], move_s)] = ']'
                return (new_coor, maze)
                



            

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
        cell = maze_arr[i][j]
        if cell == 'O':
            maze_dict[(i,2*j)] = '['
            maze_dict[(i,2*j + 1)] = ']'
        elif maze_arr[i][j] == '@':
            pos = (i,2*j)
            maze_dict[(i,2*j)] = '@'
            maze_dict[(i,2*j + 1)] = '.'
        elif maze_arr[i][j] == '.':
            maze_dict[(i,2*j)] = '.'
            maze_dict[(i,2*j + 1)] = '.'
        else:
            maze_dict[(i,2*j)] = '#'
            maze_dict[(i,2*j + 1)] = '#'

        j += 1
    i += 1
print(pos)

for line in instructions:
    for s in line:
        move = calc_move_collision(pos, s, maze_dict)
        pos = move[0]
        #print(pos)
        maze_dict = move[1]

#map all the boxes
i = 0
box_gps_coor = 0
while i < len(maze_arr):
    j = 0
    while j < 2*len(maze_arr[i]):

        if maze_dict[(i,j)] == '[':
            box_gps_coor += 100 * i + j
        j += 1
    i += 1

print(box_gps_coor)