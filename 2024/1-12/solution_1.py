# import math
# import copy
# import time

#import operator

def arr_eval(arr):
    return arr.split(" ")

with open('data.txt') as f:
    lines = f.read().splitlines()
    #lines_array = list(map(arr_eval,lines))
array_1 = []
array_2 = []

for line in lines:
    temp = line.split('   ')
    array_1.append(int(temp[0]))
    #print(first_array)
    array_2.append(int(temp[1]))

array_1.sort()
array_2.sort()

#print(array_1)

dist = 0
i = 0
while i < len(array_1):
    d = abs(array_1[i] - array_2[i])
    #print(d)
    dist += d
    i += 1

print(dist)



    






 