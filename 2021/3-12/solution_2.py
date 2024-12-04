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

lines_o2 = lines.copy()

while i < len(lines_o2[0]):
    sum = 0

    for line in lines_o2:
        sum = sum + int(line[i])
    

    if sum < len(lines_o2) / 2:
        most_common = "0"
    else:
        most_common = "1"
    new_lines = []

    for line in lines_o2:
        if line[i] == most_common:
            new_lines.append(line)
    #print(new_lines)

    lines_o2 = new_lines




    

    i = i + 1


lines_co2 = lines.copy()
i = 0
while i < len(lines_co2[0]):
    sum = 0

    for line in lines_co2:
        sum = sum + int(line[i])
    

    if sum < len(lines_co2) / 2:
        least_common = "1"
    else:
        least_common = "0"
    new_lines = []

    for line in lines_co2:
        if line[i] == least_common:
            new_lines.append(line)
    #print(new_lines)

    lines_co2 = new_lines

    i = i + 1
    if len(lines_co2) == 1:
        break

print(int(lines_co2[0],2) * int(lines_o2[0],2))













    






 