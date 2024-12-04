# import math
# import copy
# import time

#import operator

def dist(c1, c2, empty_row_index_arr, empty_col_index_arr):
    dist_before_expand = abs(c1[1] - c2[1]) + abs(c1[0] - c2[0])
    #count the number of index of row between the rows of the two stars
    # nbr_rows = len([x for x in empty_row_index_arr if x[0] in [c1[0], c2[0]]])
    # nbr_col = len([x for x in empty_col_index_arr if x[1] in [c1[1], c2[1]]])
    range_row = [c1[0], c2[0]]
    range_col = [c1[1], c2[1]]

    nbr_empty_row = 0
    nbr_empty_col = 0

    i = min(range_row)

    while i < max(range_row):
        
        if i in empty_row_index_arr:
            nbr_empty_row += 1
        i += 1

    i = min(range_col)

    while i < max(range_col):
        
        if i in empty_col_index_arr:
            nbr_empty_col += 1
        i += 1
    
    #print(range_row, nbr_empty_row, nbr_empty_col)



    return dist_before_expand + 999999 * (nbr_empty_col + nbr_empty_row)


with open('data.txt') as f:
    lines = f.read().splitlines()

empty_col_index_arr = []
#test empty col
for i in range(len(lines[0])):
    col = [row[i] for row in lines]
    if not "#" in col:
        empty_col_index_arr.append(i)


#print(empty_col_index_arr)

empty_row_index_arr = []
for i in range(len(lines)):
    if not "#" in lines[i]:
        empty_row_index_arr.append(i)

print(empty_row_index_arr)

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
        distance = dist(coor_stars[j], coor_stars[i], empty_row_index_arr,empty_col_index_arr)
        #print(coor_stars[i], coor_stars[j], dist)
        dist_arr.append(distance)
        res += distance

        j += 1

    i += 1
    
#print(dist_arr)
print(res)



    








    






 