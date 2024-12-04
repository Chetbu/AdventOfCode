# import math
# import copy
# import time





with open('data.txt') as f:
    lines = f.read().splitlines()

# for line in lines:
#     print(line)


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


# for line in lines:
#     print(line)

res = 0
i_row = 0
while i_row < len(lines):
    val = len(lines) - i_row
    nbr = lines[i_row].count("O")

    res = res + val * nbr
    i_row += 1


print(res)
 