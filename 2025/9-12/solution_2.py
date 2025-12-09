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

# print(generate_edge_rectangle2((0,0),(2,5)))
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
        
        if (min(screen_array_1) <= gap_cell[0] <= max(screen_array_1)) and (min(screen_array_0) <= gap_cell[1] <= max(screen_array_0)):
            return True
        else:
            return False


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
print(f"Time to generate tuple area list of {len(tuple_area_list)} element", time.time() - inter_time)
inter_time = time.time()        


time_edge_rectangle = 0
time_gap_array = 0
time_check_is_in = 0

i = 0
found = False
while not found:
    split_time = time.time()
    c1 = tuple_area_list[i][0]
    c2 = tuple_area_list[i][1]
    edge_array = generate_edge_rectangle(c1,c2)


    found = True
    time_edge_rectangle += time.time() - split_time
    split_time = time.time()
    for edge_c_array in edge_array:
        #check if the edge intersect with the edge of the loop

        gap_array = [c for c in edge_c_array if c not in color_dict]
        # print(gap_array)
        # print("Time to generate the gap array", time.time() - inter_time)
        # inter_time = time.time()

        split_time = time.time()

        if len(gap_array) > 0:
            gap_array_2 = [gap_array[0]]
            j = 1
            while j < len(gap_array):
                if abs(gap_array[j][0] - gap_array[j-1][0]) + abs(gap_array[j][1] - gap_array[j-1][1]) > 1:
                    gap_array_2.append(gap_array[j])

                j+=1
        else:
            gap_array_2 = []

        time_gap_array += time.time() - split_time

        # print("Number of gaps to check", len(gap_array), len(gap_array_2))
        # print("Time to generate the gap to check", time.time() - inter_time)
        # inter_time = time.time()

        #for each cell of the gap array, check if the cell is in the loop
        split_time = time.time()
        for gap_cell in gap_array_2:
            if is_in_loop(gap_cell,c_array):
                #cell is in the loop
                continue
            else:
                #cell is out of the loop, rectangle is not fully red and green
                found = False
                break
        if not found:
            break
        time_check_is_in += time.time() - split_time
        split_time = time.time()

    if found:
        print(f"Max area is {tuple_area_list[i][2]}")
    if i % 100 == 0:
        print("Time to check 100 rectangles", time.time() - inter_time, "edge time : ", time_edge_rectangle, "gap generation time :" , time_gap_array, "Time check is in :", time_check_is_in)
        time_edge_rectangle = 0
        time_gap_array = 0
        time_check_is_in = 0
        inter_time = time.time()

    i += 1



print("Time to check the rectangle", time.time() - inter_time)
inter_time = time.time()  

print("Total time", time.time() - start_time)
 