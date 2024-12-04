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

def forecast_arr(arr):
    i = len(arr) - 2
    #print(arr[-1])
    arr[-1].append(0)
    while i >= 0:
        #next_increment = arr[i+1][-1]
        arr[i].append(arr[i][-1] + arr[i+1][-1])
        i = i - 1
    return arr


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
    forecast_arr(res_line_array)
    #print(forecast_arr(res_line_array))
    res = res + res_line_array[0][-1]

print(res)



    








    






 