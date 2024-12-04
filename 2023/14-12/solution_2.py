# import math
# import copy
# import time
#from functools import lru_cache

#@lru_cache
def move_rock_north(lines_t):
    lines = list(lines_t)
    i_col = 0
    while i_col < len(lines[0]):
        i_row = 0
        i_available_space = 0
        empty_space_above = False
        while i_row < len(lines):
            char = lines[i_row][i_col]
            #print(char, empty_space_above)
            if char == "#":
                #unmovable rock, no empty space above
                empty_space_above = False
            elif char == "O" and not empty_space_above:
                #same situation, rock has moved already to the new spot or is in a north spot
                empty_space_above = False
            elif char == "." and not empty_space_above:
                #first space available of the col
                empty_space_above = True
                i_available_space = i_row
            elif char == "O" and empty_space_above:
                #let's move the rock, put the 0 at i_available and a "." at current i
                #print(lines[i_row])
                lines[i_row] = lines[i_row][:i_col] + "." + lines[i_row][i_col + 1:]
                #print(lines[i_row])
                #print(lines[i_available_space], i_available_space)
                lines[i_available_space] = lines[i_available_space][:i_col] + "O" + lines[i_available_space][i_col + 1:]

                #reset i to i available and empty space to False
                i_row = i_available_space
                empty_space_above = False


            i_row += 1
        i_col += 1
    return tuple(lines)

#@lru_cache
def lines_rotate(arr):
    new_arr = []
    for j in range(len(arr[0])):
        s = ""
        i = len(arr) - 1
        while i >= 0:
            s += arr[i][j]
            i -= 1
        new_arr.append(s)
    return tuple(new_arr)

def eval_weight(lines_t):
    res = 0
    i_row = 0

    while i_row < len(lines_t):
        val = len(lines_t) - i_row
        nbr = lines_t[i_row].count("O")

        res = res + val * nbr
        i_row += 1

    return res

def perform_cycle(lines_t):
    i = 0
    while i < 4:
        lines_t = move_rock_north(lines_t)
        lines_t = lines_rotate(lines_t)
        i+= 1
    return lines_t
    

with open('data.txt') as f:
    lines = f.read().splitlines()
    


lines_t = tuple(lines)
# test_lines = tuple(lines)

# print(eval_weight(move_rock_north(test_lines)))

# nbr_cycle = 0
# limit_cycle = 3

# while nbr_cycle < limit_cycle:
#     # for rot in range(4):
#     #     test_lines = move_rock_north(test_lines)
#     #     test_lines = lines_rotate(test_lines)
#     #     #print(rot)
#     test_lines = perform_cycle(test_lines)
#     nbr_cycle += 1

# for line in test_lines:
#     print(line)

nbr_cycle = 0
limit_cycle = 1000000000

storage = []
storage_nbr_cycle = []
rec_found = False
l_cycle = -1
while nbr_cycle < limit_cycle and not rec_found:
    lines_t = perform_cycle(lines_t)

    nbr_cycle += 1
    if not lines_t in storage:
        storage.append(lines_t)
        storage_nbr_cycle.append(nbr_cycle)
    else:
        rec_found = True
        l_cycle = nbr_cycle - storage_nbr_cycle[storage.index(lines_t)]
        print("recurrence at", nbr_cycle, "with", storage_nbr_cycle[storage.index(lines_t)], "l_cycle = ", l_cycle)

while nbr_cycle < limit_cycle:
    nbr_cycle += l_cycle
    #print(nbr_cycle)

nbr_cycle -= 2*l_cycle

while nbr_cycle < limit_cycle:
    lines_t = perform_cycle(lines_t)
    nbr_cycle += 1

#print(limit_cycle, nbr_cycle)


print(eval_weight(lines_t))
 