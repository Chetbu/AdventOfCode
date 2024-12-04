# import math
# import copy
# import time

#import operator

def difference_array(arr):
    i = 1
    diff_arr = []
    while i < len(arr):
        diff_arr.append(arr[i] - arr[i - 1])
        i = i + 1
    return diff_arr

def backcast_arr(arr):
    i = len(arr) - 2
    #print(arr)
    inc = 0

    while i >= 0:
        #print(arr[i][0], inc)
        inc = arr[i][0] - inc
        i = i - 1
        #print(inc)
    return inc


with open('data.txt') as f:
    lines = f.read().splitlines()

line_array = []
for line in lines:

    l = line.split(" ")
    i = 0
    l_res = []
    while i < len(l):
        l_res.append(int(l[i]))
        i = i + 1
    line_array.append(l_res)

#print(line_array)
res = 0
for line in line_array:
    res_line_array = [line]
    current_line = line
    while current_line.count(0) != len(current_line):
        current_line = difference_array(current_line)
        res_line_array.append(current_line)
    #print(res_line_array)
    backcast_arr(res_line_array)
    #print(new_arr)
    res = res + backcast_arr(res_line_array)

print(res)



    








    






 