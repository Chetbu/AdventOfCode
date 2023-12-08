# import math
# import copy
# import time


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
    return map[coor[1][0]][coor[1][1]]


def edge_teleport(coor:tuple, map:list):
    new_coor = coor
    while eval_map(new_coor, map) == " ":
        temp_coor = take_1_step(new_coor)
        new_coor = (
            temp_coor[0], (
                (len(map)  + temp_coor[1][0]) % len(map),
                (len(map[0])  + temp_coor[1][1]) % len(map[0])
            )
        )
        #print(new_coor)
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



print(step_list)
# test_c = ("N", (1,10))
# print(take_X_steps(test_c,2,maze))

launch_c = ("E", (1,1))
coor = edge_teleport(launch_c, maze)
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




