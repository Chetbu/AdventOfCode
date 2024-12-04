# import math
# import copy
# import time

#import operator

def arr_eval(arr, char):
    return arr.split(char)


with open('data.txt') as f:
    lines = f.read().splitlines()

line_array = []
for line in lines:

    l = line.split(" ")
    while "" in l:
        l.remove("")
    i = 1
    l_res = []
    while i < len(l):
        l_res.append(int(l[i]))
        i = i + 1
    line_array.append(l_res)

#print(line_array)

i = 0
res = 1
while i < len(line_array[0]):
    j = 0
    distance_arr = []
    count_best = 0
    while j < line_array[0][i]:
        distance = j * (line_array[0][i] - j)
        distance_arr.append(distance)
        if distance> line_array[1][i]:
            count_best = count_best + 1 

        j = j + 1
    #print(count_best)
    res = res * count_best
    i = i + 1

print(res)


    








    






 