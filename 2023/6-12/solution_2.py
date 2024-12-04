# import math
# import copy
import time

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
    l_res = ""
    while i < len(l):
        l_res = l_res + l[i]
        i = i + 1
        #print(l_res)
    line_array.append(int(l_res))


i = 0
res = 1

j = 0

start = time.time()

count_best = 0
while j < line_array[0]:
    distance = j * (line_array[0] - j)

    if distance> line_array[1]:
        count_best = count_best + 1 

    j = j + 1
#print(count_best)
res = res * count_best


print(res)
print("one done", time.time()-start)


    








    






 