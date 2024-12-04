# import math
# import copy
# import time

tiles = [".", "-", "|", "/", chr(92) ]
dir = ["N", "E", "S", "W"]

dir_inc_arr = [(-1,0), (0,1), (1,0), (0,-1)]

next_dir_arr = [
    ["N", "WE", "N", "E", "W"],
    ["E", "E", "NS", "N", "S"],
    ["S", "WE", "S", "W", "E"],
    ["W", "W", "NS", "S", "N"],

]

def move_next_coor(coor,next_dir):

    dir_inc = dir_inc_arr[dir.index(next_dir)]
    next_coor = (
        coor[0] + dir_inc[0],
        coor[1] + dir_inc[1]
    )

    return (next_coor, next_dir)


def next_move(move,grid):
    coor = move[0]
    direction = move[1]
    current_tile = grid[coor[0]][coor[1]]

    i_tile = tiles.index(current_tile)
    i_direction = dir.index(direction)

    next_dir = next_dir_arr[i_direction][i_tile]
    if len(next_dir) > 1:
        #split in two case
        next_dir_1 = next_dir[0]
        next_dir_2 = next_dir[1]
        return [move_next_coor(coor, next_dir_1) , move_next_coor(coor, next_dir_2)]
    else:
        return [move_next_coor(coor, next_dir)]

def is_in_grid(move, grid):
    coor = move[0]
    return 0 <= coor[0] < len(grid) and 0 <= coor[1] < len(grid[0])

    


with open('test.txt') as f:
    lines = f.read().splitlines()

print(lines)

# print(ord(lines[0][5]))
# print(chr(92) == lines[0][5])



move_array = [((0,0), "E")]
i = 0

while i < len(move_array):
    current_move = move_array[i]
    print(current_move)
    if is_in_grid(current_move, lines):
        new_moves = next_move(current_move,lines)
        for m in new_moves:
            if not m in move_array:
                move_array.append(m)
        i += 1
    else:
        del move_array[i]


print(move_array)

#extract the coord array
tiles = []
for m in move_array:
    coor = m[0]
    if not coor in tiles:
        tiles.append(coor)

print(len(tiles))

