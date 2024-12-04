# import math
# import copy
# import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)

dir_arr = (
    (0,1),
    (0,-1),
    (1,0),
    (-1,0),
    (1,1),
    (-1,-1),
    (1,-1),
    (-1,1)
)

expected_result = "XMAS"

def search_result(x : int,y : int , matrix, dir : tuple, expected_res : str):
    x_maximum = len(matrix)
    y_maximum = len(matrix[0])
    i = 0
    found = True
    while i < len(expected_res):
        x_i = x + i * dir[0]
        y_i = y + i * dir[1]
        #print(x_i, y_i)
        if not(0 <= x_i < x_maximum) or not(0 <= y_i < y_maximum):
            return False
        elif matrix[x_i][y_i] != expected_res[i]:
            return False
        else:
            i += 1
    return found

file_filepath = Path(current_dir, "data.txt")

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

i = 0
j = 0

total_count = 0

while i < len(lines):
    j = 0
    while j < len(lines[i]):
        if lines[i][j] == "X":
            count = 0
            for dir in dir_arr:
                temp = search_result(i,j,lines,dir,expected_result)
                if temp:
                    count += 1
            total_count += count

        j += 1
    i += 1



print(total_count)


 