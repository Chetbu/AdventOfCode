# import math
# import copy
# import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)

def search_result(x : int,y : int , matrix):

    #check first & second diag
    first_diag = matrix[x - 1][y - 1] + matrix[x][y] +  matrix[x + 1][y + 1]
    second_diag = matrix[x + 1][y - 1] + matrix[x][y] +  matrix[x - 1][y + 1]
    possible_solution_arr = ["MAS", "SAM"]
    return first_diag in possible_solution_arr and second_diag in possible_solution_arr


file_filepath = Path(current_dir, "data.txt")

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

i = 1
j = 1

total_count = 0

while i < len(lines) - 1:
    j = 1
    while j < len(lines[i]) - 1:
        if lines[i][j] == "A":

            if search_result(i,j,lines):
                total_count += 1

        j += 1
    i += 1



print(total_count)


 