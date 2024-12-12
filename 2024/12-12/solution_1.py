#import math
import copy
import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

dir_arr = (
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
)

def calc_fences(coor_t, string_arr, dir_arr):
    x = coor_t[0]
    y = coor_t[1]
    value = string_arr[x][y]
    fence_count = 0
    for dir in dir_arr:
        x1 = x + dir[0]
        y1 = y + dir[1]
        if 0 <= x1 < len(string_arr) and 0 <= y1 < len(string_arr[0]):
            if string_arr[x1][y1] != value:
                # fence
                fence_count += 1
        else:
            fence_count += 1
    return fence_count

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)
fenced_array = []
x = 0
while x < len(lines):
    y = 0
    while y < len(lines[x]):
        fenced_array.append(((x,y),lines[x][y],calc_fences((x,y), lines, dir_arr)))
        y += 1
    x += 1
#print(fenced_array)
total_price = 0
while len(fenced_array) > 0:
    first_element = fenced_array[0]
    value = first_element[1]
    #search for neighbours in the array
    
    region_coor_array = [first_element[0]]
    i = 0
    while i < len(region_coor_array):
        current_plot_coor = region_coor_array[i]
        for dir in dir_arr:
            x1 = region_coor_array[i][0] + dir[0]
            y1 = region_coor_array[i][1] + dir[1]
            if 0 <= x1 < len(lines) and 0 <= y1 < len(lines[0]) and not((x1,y1) in region_coor_array) and lines[x1][y1] == value:
                region_coor_array.append((x1,y1))


        i += 1
    #print(region_coor_array)

    area = len(region_coor_array)
    fence_length = 0
    for plot in region_coor_array:
        index_plot = [x[0] for x in fenced_array].index(plot)
        fenced_plot = fenced_array.pop(index_plot)
        fence_length += fenced_plot[2]
    #print(area, fence_length, area * fence_length)
    total_price += area * fence_length

print(total_price)


