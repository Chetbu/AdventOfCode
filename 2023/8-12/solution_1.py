# import math
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


num_step = 0
goal = "ZZZ"
current_node = "AAA"
while current_node != goal:
    index_node = coord_array.index(current_node)
    map_node = line_array[index_node]
    current_node = next_node(num_step, map_node)
    #print(current_node)
    num_step = num_step + 1

print(num_step)

    







    








    






 