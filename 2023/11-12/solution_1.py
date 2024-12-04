# import math
# import copy
# import time

#import operator

with open('data.txt') as f:
    lines = f.read().splitlines()

empty_col_index_arr = []
#test empty col
for i in range(len(lines[0])):
    col = [row[i] for row in lines]
    if not "#" in col:
        empty_col_index_arr.append(i)

#print(empty_col_index_arr)

#enlarge the picture
i_col = len(empty_col_index_arr) - 1
while i_col >= 0:
    #print(i)
    col_index = empty_col_index_arr[i_col]
    for i in range(len(lines)):
        #print(lines[i][:col_index])
        lines[i] = lines[i][:col_index] + "." + lines[i][col_index:]
        #print(len(lines[i]))
    i_col -= 1

new_l = len(lines[0])
empty_line = ""
for i in range(new_l):
    empty_line += "."


i = 0
while i < len(lines):
    if not "#" in lines[i]:
        lines.insert(i, empty_line)
        i += 1

    i += 1

coor_stars = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            coor_stars.append((i,j))

print(coor_stars)
dist_arr = []
res = 0

# for line in lines:
#     print(line)

i = 1
while i < len(coor_stars):
    j = 0
    while j < i:
        dist = abs(coor_stars[j][1] - coor_stars[i][1]) + abs(coor_stars[j][0] - coor_stars[i][0])
        #print(coor_stars[i], coor_stars[j], dist)
        dist_arr.append(dist)
        res += dist

        j += 1

    i += 1
    
#print(dist_arr)
print(res)



    








    






 