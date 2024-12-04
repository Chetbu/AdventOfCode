# import math
# import copy
# import time

#import operator

def arr_eval(arr):
    return arr.split(" ")

with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_eval,lines))

#print(lines_array)

pos = [0,0,0]

move_set = (
    ("down", (0,0,-1)),
    ("up", (0,0,1))
)

for move in lines_array:
    #print(move)
    forward_bool = True
    for i in range(len(move_set)):
        #print(move_set[i][0])
        if move_set[i][0] == move[0]:
            forward_bool = False
            pos[2] = pos[2] + int(move[1]) * move_set[i][1][2]
    if forward_bool:
        pos[0] = pos[0] + int(move[1])
        pos[1] = pos[1] + int(move[1]) * pos[2]
    #print(pos)

print(pos)
print(pos[0] * pos[1])










    






 