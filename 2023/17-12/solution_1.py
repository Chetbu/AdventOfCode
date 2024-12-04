# import math
# import copy
# import time

#tuple to represent the state (x,y,origin_dir,nbr times on this dir, total_score)

dir = ("N", "E", "S", "W")
invert_dir = ("S", "W", "N", "E")
dir_inc_arr = ((-1,0), (0,1), (1,0), (0,-1))

def next_move(move, direction, grid):
    i_dir = dir.index(direction)
    dir_inc = dir_inc_arr[i_dir]
    count = move[3]

    new_coor_x = move[0] + dir_inc[0] 
    new_coor_y = move[1] + dir_inc[1]

    if move[2] == direction:
        count += 1
    else:
        count = 1

    if count > 3:
        eval = 1000000000
    else:
        eval = move[4] + int(grid[new_coor_x][new_coor_y])
    return (
        new_coor_x,
        new_coor_y,
        direction,
        count,
        eval
    )

def possible_directions(move, grid):
    pos_dir_array = list(dir)
    i_dir = dir.index(move[2])
    opposite_direction = invert_dir[i_dir]
    pos_dir_array.remove(opposite_direction)

    if move[3] == 3:
        pos_dir_array.remove(move[2])
    
    res = []
    for d in pos_dir_array:
        j_dir = dir.index(d)

        dir_inc = dir_inc_arr[j_dir]
        new_coor_x = move[0] + dir_inc[0] 
        new_coor_y = move[1] + dir_inc[1]
        if coor_in_grid(new_coor_x, new_coor_y, grid):
            res.append(next_move(move, d, grid))
    return res

def coor_in_grid(x,y,grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

with open('data.txt') as f:
    lines = f.read().splitlines()

#print(lines)

first_move = (0,0,"E",0,0)
move_array = [first_move]

lowest_value_dict = dict()
#print(first_move[:4])
lowest_value_dict[first_move[:4]] = first_move[-1]

i = 0
finish_coor = (len(lines) -1, len(lines[0])-1)
#print(finish_coor)

#first solution to be the diagonal
j = 1
first_solution = 0
while j < finish_coor[0]:
    first_solution += int(lines[j-1][j])
    first_solution += int(lines[j][j])
    j += 1
#print(j, first_solution)

finish_eval_arr = []
finish_eval_min = first_solution

while len(move_array) > 0:
    current_move = move_array.pop(0)
    new_move_arr = possible_directions(current_move, lines)
    add_move_arr = []
    for m in new_move_arr:
        if m[:2] == finish_coor:
            finish_eval_arr.append(m[-1])
            finish_eval_min = min(finish_eval_min, m[-1])

        elif m[:4] in lowest_value_dict and m[-1] <= finish_eval_min:
            lowest_record = lowest_value_dict.get(m[:4])
            if lowest_record > m[-1]:
                lowest_value_dict[m[:4]] = m[-1]
                add_move_arr.append(m)
        elif m[-1] <= finish_eval_min:
            lowest_value_dict[m[:4]] = m[-1]
            add_move_arr.append(m)



    move_array = move_array + add_move_arr
    i += 1
    if i % 1000 == 0:

        #sort move so it is first as far away as we can
        move_array.sort()
        #print(move_array)
        print(i, len(move_array), len(finish_eval_arr), len(lowest_value_dict), move_array[0][:2])
#print(move_array)
#print(min(finish_eval_arr))
        
print(finish_eval_min)




