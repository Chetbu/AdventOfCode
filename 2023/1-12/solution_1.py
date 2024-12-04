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

res = 0
for word in lines:
    i = 0
    while not word[i].isdigit(): 
        i = i + 1
    j = len(word) -1
    while not word[j].isdigit(): 
        j =j -1 
    res = res + 10 * int(word[i]) + int(word[j])

print(res)





    






 