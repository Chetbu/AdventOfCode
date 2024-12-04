# import math
# import copy
# import time

#import operator

def arr_eval(arr):
    return arr.split(" ")

with open('data.txt') as f:
    lines = f.read().splitlines()
    #lines_array = list(map(arr_eval,lines))

#print(lines)
i = 0
gamma = ""
epsilon = ""
while i < len(lines[0]):
    sum = 0

    for line in lines:
        sum = sum + int(line[i])
    

    if sum <= len(lines) / 2:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
    else:
        gamma = gamma + "1"
        epsilon = epsilon + "0"

    i = i + 1

#print(gamma)
#print(int(epsilon,2))

print(int(gamma,2) * int(epsilon,2))














    






 