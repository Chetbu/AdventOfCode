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
    (1,0),
    (0,-1),
    (-1,0)
)

def calc_fences(coor_t, string_arr, dir_arr):
    x = coor_t[0]
    y = coor_t[1]
    value = string_arr[x][y]
    fence_arr = []
    for dir in dir_arr:
        x1 = x + dir[0]
        y1 = y + dir[1]
        if 0 <= x1 < len(string_arr) and 0 <= y1 < len(string_arr[0]):
            if string_arr[x1][y1] != value:
                # fence
                fence_arr.append(1)
            else:
                fence_arr.append(0)
        else:
            fence_arr.append(1)
    return fence_arr

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

#pre-calculate the fence needed (in an array related to the dir arr)
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
    side_array = []
    for plot in region_coor_array:
        index_plot = [x[0] for x in fenced_array].index(plot)
        fence_plot_arr = fenced_array[index_plot][2]
        side_i = 0
        while side_i < len(fence_plot_arr):
            if fence_plot_arr[side_i] == 1:
                #a fence in on this side, need to check the neighbors for mapping a side
                #explore the two sides
                dir_explore_arr = [dir_arr[(side_i + 1) % 4], dir_arr[(side_i + 3) % 4]]
                side_coor_array = [plot]
                for dir in dir_explore_arr:
                    i = 1
                    stay_on = True
                    while stay_on:
                        next_x = plot[0] + dir[0] * i
                        next_y = plot[1] + dir[1] * i
                        stay_on = False
                        if (next_x, next_y) in region_coor_array:
                            index_next_plot = [x[0] for x in fenced_array].index((next_x, next_y))
                            #check if there is a fence on the same side
                            if fenced_array[index_next_plot][2][side_i] == 1:
                                side_coor_array.append((next_x, next_y))
                                stay_on = True
                                i += 1

                #sort and create the tuple to make it comparable easily with existing sides calculated
                side_coor_array.sort()
                side_t = (side_i, tuple(side_coor_array))
                #print(side_t)
                if not(side_t in side_array):
                    side_array.append(side_t)

            side_i += 1

    total_price += len(side_array) * area

    #delete all the plot in region from fence_arr
    for plot in region_coor_array:
        index_plot = [x[0] for x in fenced_array].index(plot)
        del fenced_array[index_plot]


print(total_price, time.time() - start_time)

