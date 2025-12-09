import math
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()
inter_time = time.time()

def generate_edge_rectangle(c0,c1):
    # create a list of all the tuple between c1 and c2
    x_0 = min(c0[0], c1[0])
    x_1 = max(c0[0], c1[0])
    y_0 = min(c0[1], c1[1])
    y_1 = max(c0[1], c1[1])

    t1 = []
    t2 = []
    t3 = []
    t4 = []

    for x in range(x_0, x_1 + 1, 1):
        t1.append((x,y_0))
        t2.append((x,y_1))
    for y in range(y_0, y_1 + 1, 1):
        t3.append((x_0, y))
        t4.append((x_1,y))
    res = [t1,t2,t3,t4]
    return res

cache_dict = {}
def is_in_loop(gap_cell, c_array):
        if (gap_cell[0],0) in cache_dict:
            screen_array_0 = cache_dict[(gap_cell[0],0)]
        else:
            screen_array_0 = [c[1] for c in c_array if c[0] == gap_cell[0]]
            cache_dict[(gap_cell[0],0)] = screen_array_0
        if (0,gap_cell[1]) in cache_dict:
            screen_array_1 = cache_dict[(0,gap_cell[1])]
        else:
            screen_array_1 = [c[0] for c in c_array if c[1] == gap_cell[1]]
            cache_dict[(0,gap_cell[1])] = screen_array_1
        if len(screen_array_1) == 0 or len(screen_array_0) == 0:
            return False
        elif (min(screen_array_1) <= gap_cell[0] <= max(screen_array_1)) and (min(screen_array_0) <= gap_cell[1] <= max(screen_array_0)):
            return True
        else:
            return False



def explore_from_node(node, c_array, color_dict):
    res = []
    dir_array = ((0,1), (0,-1), (1,0), (-1,0))
    for dir in dir_array:
        step = 1
        keep_explore = True
        segment_tested = False
        while keep_explore:
            current_c = (node[0] + step * dir[0], node[1] + step * dir[1])
            if current_c in color_dict:
                segment_tested = False
                step += 1
            elif segment_tested:
                # color_dict[current_c] = "G"
                step += 1
            elif is_in_loop(current_c, c_array):
                # color_dict[current_c] = "G"
                segment_tested = True
                step += 1
            else:
                keep_explore = False
        step -= 1
        max_coord = (node[0] + step * dir[0], node[1] + step * dir[1])
        res.append(max_coord)
    return tuple(res)

def is_in_segment(point, start_seg, end_seg):
    if point[0] == start_seg[0] and point[0] == end_seg[0]:
        if min(start_seg[1], end_seg[1]) <= point[1] <= max(start_seg[1], end_seg[1]):
            return True
        else:
            return False
    elif point[1] == start_seg[1] and point[1] == end_seg[1]:
        if min(start_seg[0], end_seg[0]) <= point[0] <= max(start_seg[0], end_seg[0]):
            return True
        else:
            return False
    return False

# print("is_in_segment ", is_in_segment((3,0),(1,0),(5,0)))
# print("is_in_segment ", is_in_segment((6,0),(1,0),(5,0)))
# print("is_in_segment ", is_in_segment((0,5),(0,0),(0,10)))
# print("is_in_segment ", is_in_segment((0,15),(0,0),(0,10)))



with open(file_filepath) as f:
    lines = f.read().splitlines()

coord_array = [(int(x[0]), int(x[1])) for x in [y.split(',') for y in lines]]
#Close the loop
coord_array.append(coord_array[0])
# print(coord_array)

print("Time to generate the corner coord", time.time() - inter_time)
inter_time = time.time()

color_dict = {}
color_dict[coord_array[0]] = "R"

c_array = [coord_array[0]]
i = 1
while i < len(coord_array):
    c0 = coord_array[i - 1]
    c1 = coord_array[i]
    color_dict[c1] = "R"
    #spot all the tiles between c1 and c2 and make them green
    if c0[0] == c1[0]:
        increment = (0, -int((c0[1] - c1[1])/abs(c0[1] - c1[1])))
    else:
        increment = (-int((c0[0] - c1[0])/abs(c0[0] - c1[0])), 0)
    c_current = (c0[0] + increment[0], c0[1] + increment[1])
    while c_current != c1:
        c_array.append(c_current)
        color_dict[c_current] = "G"
        c_current = (c_current[0] + increment[0], c_current[1] + increment[1])
        
    c_array.append(c1)
    i += 1


#remove last element as it is duplicate
del c_array[-1]

print("Time to generate the edge coord of the loop", time.time() - inter_time)
inter_time = time.time()

i = 0
tuple_area_list = []
while i < len(coord_array) - 1:
    j = i + 1
    while j < len(coord_array):
        #calc the area of the rectangle
        c1 = coord_array[i]
        c2 = coord_array[j]
        area = abs(c1[0] - c2[0] + 1) * abs(c1[1] - c2[1] + 1)
        tuple_area_list.append((c1,c2,area))
        j += 1
    i += 1

tuple_area_list.sort(key= lambda tup: tup[2], reverse=True)
# print(tuple_area_list)
print(f"Time to generate tuple area list of {len(tuple_area_list)} element", time.time() - inter_time)
inter_time = time.time()        


#For each red, calculate the max distance in each direction where the segment is green or red
max_range_dict = {}
for red_cell in coord_array:
    # print(red_cell, explore_from_node(red_cell, c_array,color_dict))
    max_range_dict[red_cell] = explore_from_node(red_cell, c_array,color_dict)

print(f"Time to generate max distance dict", time.time() - inter_time)
inter_time = time.time() 

i = 0
found = False
while not found:
    c1 = tuple_area_list[i][0]
    c2 = tuple_area_list[i][1]
    max_range_c1_array = max_range_dict[c1]
    max_range_c2_array = max_range_dict[c2]

    #Calculate the opposite corners    
    opposite_corners = [(c1[0], c2[1]), (c2[0], c1[1])]

    link_count = 0
    for c in opposite_corners:
        #for each opposite corner, check if they are connected by green / red tiles to the 2 other corners
        linked_c1 = False
        for max_range_c in max_range_c1_array:
            #if there is one of 4 segment where the point is connected, it is considered linked
            if is_in_segment(c, c1, max_range_c):
                linked_c1 = True
        linked_c2 = False
        for max_range_c in max_range_c2_array:
            if is_in_segment(c, c2, max_range_c):
                linked_c2 = True
        if linked_c1 and linked_c2:
            # If the point is link to c1 and c2, means that this part of the rectangle is complete
            link_count += 1

    #if both points are connected to c1 and c2, rectangle is good !
    if link_count == 2:
        print(f"Max area is {tuple_area_list[i][2]}")
        found = True
    i += 1

print("Total time", time.time() - start_time)