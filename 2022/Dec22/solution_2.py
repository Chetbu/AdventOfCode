# import math
# import copy
# import time
import sys


# def arr_eval(arr):
#     return arr.split(" ")

def change_direction(coor:tuple, rotation:str): #change direction
    initial_dir = coor[0]
    dir_array = ["N","E","S","W"]
    i = dir_array.index(initial_dir)
    if rotation == "L":
        i = i - 1
    elif rotation == "R":
        i = (i + 1) % len(dir_array)
    return (dir_array[i], coor[1])


def take_1_step(coor:tuple): #take one step into a direction
    direction = coor[0]
    dir = (
        ("S", (1,0)), #South
        ("N", (-1,0)), #North
        ("E", (0,1)), #East
        ("W", (0,-1)) #West
    )
    i_dir = 0
    while direction != dir[i_dir][0]:
        i_dir += 1
    
    new_coor_x = coor[1][0] + dir[i_dir][1][0]
    new_coor_y = coor[1][1] + dir[i_dir][1][1]
    return (direction, (new_coor_x, new_coor_y))

def take_X_steps(coor:tuple, X:int, map:list):
    i = X
    c = coor
    while i > 0:
        temp_c = take_1_step(c)
        sq = eval_map(temp_c, map)
        if sq == " ":
            temp_c = edge_teleport(temp_c,map)
            if eval_map(temp_c,map) != "#":
                c = temp_c
            else:
                i = 0
        elif sq == "#":
            i = 0
        else:
            c = temp_c
        i -= 1
    return c

def eval_map(coor:tuple,map:list): #eval_the char on the map
    try: 
        return map[coor[1][0]][coor[1][1]]
    except:
        print(coor[1][0],coor[1][1])
        sys.exit(1)


def edge_teleport(coor:tuple, map:list):
    direction = coor[0]
    new_x = -1000
    new_y = -1000

    old_x = coor[1][0]
    old_y = coor[1][1]
    #first edge
    if 1 <= old_x <= 50 and old_y == 151: #check
        #right side of 1, goes to right side of 4
        direction = "W"
        new_y = 100
        new_x = 151 - old_x
    elif 101 <= old_x <= 150 and old_y == 101: #check
        #right side of 4, goes to right side of 1
        direction = "W"
        new_y = 150
        new_x = 151 - old_x
    elif old_x == 51 and 101 <= old_y <= 150 and coor[0] == "S": #check
        #bottom of 1, goes into the right side of 3
        direction = "W"
        new_y = 100
        new_x = old_y - 50
    elif 51 <= old_x <= 100 and old_y == 101 and coor[0] == "E":
        #Right of 3, goes into the bottom on one
        direction = "N"
        new_x = 50
        new_y = old_x + 50
    elif old_x == 151 and 51 <= old_y <= 100 and coor[0] == "S":
        #bottom of 4, goes into the right side of 6
        direction = "W"
        new_y = 50
        new_x = old_y + 100
    elif 151 <= old_x <= 200 and old_y == 51 and coor[0] == "E":
        #Right of 6, goes into the bottom on 4
        direction = "N"
        new_x = 150
        new_y = old_x -100
    elif old_x == 100 and 1 <= old_y <= 50 and coor[0] == "N":
        #top of 5, goes into the left of 3
        direction = "E"
        new_y = 51
        new_x = old_y + 50
    elif 51 <= old_x <= 100 and old_y == 50 and coor[0] == "W":
        #left of 3, goes into the top of 5
        direction = "S"
        new_x = 101
        new_y = old_x - 50
    elif 101 <= old_x <= 150 and old_y == 0:
        #left side of 5, goes to left side of 2
        direction = "E"
        new_y = 51
        new_x = 151 - old_x
    elif 1 <= old_x <= 50 and old_y == 50:
        #left side of 2, goes to left side of 5
        direction = "E"
        new_y = 1
        new_x = 151 - old_x
    elif old_x == 0 and 51 <= old_y <= 100:
        #top side of 2, goes to left side of 6
        direction = "E"
        new_y = 1
        new_x = old_y + 100
    elif 151 <= old_x <= 200 and old_y == 0:
        #left of 6, goes to top side of 2
        direction = "S"
        new_x = 1
        new_y = old_x - 100
    elif old_x == 0 and 101 <= old_y <= 150:
        #top side of 1, goes to bottom side of 6
        direction = "N"
        new_y = old_y - 100
        new_x = 200
    elif old_x == 201 and 1 <= old_y <= 50:
        #bottom side of 6, goes to top side of 1
        direction = "S"
        new_y = old_y + 100
        new_x = 1
    else:
        ValueError("Edge not found")

    new_coor = (direction, (new_x, new_y))

    print("old_coor :", coor, " new_coor :", new_coor)
    return new_coor

    


with open('data.txt') as f:
    lines = f.read().splitlines()

    maze = lines[:-2]
    steps = lines[-1]
#make evry line as long as the max and #add blank up, down left and right
max_l = 0
for line in maze:
    max_l = max(max_l, len(line))

i = 0
while i < len(maze):
    maze[i] = " " + maze[i] + " " * (max_l - len(maze[i]) + 1)
    i += 1


maze.insert(0, " " * len(maze[0]))
maze.append(" " * len(maze[0]))

#print(maze)

step_list = []
i = 0
#steps begin and end with a number
while i < len(steps):
    j = i
    while j < len(steps) and not(steps[j] in ["L", "R"]):
        j += 1
    step_list.append(int(steps[i:j]))
    if not(j == len(steps)):
        step_list.append(steps[j])

    i = j + 1



#print(step_list)
# test_c = ("N", (1,10))
# print(take_X_steps(test_c,2,maze))

launch_c = ("E", (1,1))
coor = ("E", (1,51))
i = 0
while i < len(step_list):
    if step_list[i] in ["L","R"]:
        coor = change_direction(coor, step_list[i])
    else:
        coor = take_X_steps(coor, step_list[i],maze)
    i += 1

print(coor)
dir_val = (
    ("S", 1), #South
    ("N", 3), #North
    ("E", 0), #East
    ("W", 2) #West
)

i = 0
while dir_val[i][0] != coor[0]:
    i+=1

res = 1000 * coor[1][0] + 4 * coor[1][1] + dir_val[i][1]
print(res)




