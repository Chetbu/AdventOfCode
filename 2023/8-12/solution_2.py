import math
# import copy
# import time

#import operator

def arr_eval(arr, char):
    return arr.split(char)

def next_node(num, map):
    i = num % len(instructions)
    if instructions[i] == "L":
        return map[1][0]
    else:
        return map[1][1]


with open('data.txt') as f:
    lines = f.read().splitlines()

instructions = lines[0]
line_array = []
coord_array = []
i = 2
while i < len(lines):
    split = lines[i].split(" ")
    line_array.append(
        (
            split[0],
            (split[2][1:-1],split[3][:-1])
         )
    )
    coord_array.append(split[0])

    i = i + 1

#print(line_array)
end_array = []
current_node_array = []
i = 0
while i < len(coord_array):
    if coord_array[i][2] == "A":
        current_node_array.append(coord_array[i])
    elif coord_array[i][2] == "Z":
        end_array.append(coord_array[i])
    
    i = i + 1



#current_node_array = current_node_array[:2]
print(current_node_array)


start_end_array = []

step_to_end = [len(instructions)]

for i in range(len(current_node_array)):
    current_end_arr = []
    for j in range(len(end_array)):
        num_step = 0
        goal = end_array[j]
        current_node = current_node_array[i]
        while current_node != goal:
            index_node = coord_array.index(current_node)
            map_node = line_array[index_node]
            current_node = next_node(num_step, map_node)
            #print(current_node)
            num_step = num_step + 1
            if num_step == 100000:
                num_step = -1
                break
        current_end_arr.append(num_step)
        if num_step > 0:
            step_to_end.append(num_step)
    start_end_array.append(current_end_arr)


print(start_end_array)
print(step_to_end)
print(math.lcm(293, 19631, 13771, 21389, 17287, 23147, 20803))
lcm_res = math.lcm(step_to_end[0],step_to_end[1])
i = 2
while i < len(step_to_end):
    lcm_res = math.lcm(step_to_end[i],lcm_res)
    i = i + 1 
print(lcm_res)

    







    








    






 