# import math
# import copy
# import time

#import operator

def arr_eval(arr, char):
    return arr.split(char)

with open('data.txt') as f:
    lines = f.read().splitlines()


#print(lines)
#print(ord(lines[0][0]))

index_l = 0

number_arr = []
possible_gear_arr = []
pos_arr = []
while index_l < len(lines):
    i = 0
    while i < len(lines[index_l]):
        if lines[index_l][i].isdigit():
            l = 0
            while lines[index_l][i + l].isdigit():
                if i + l == len(lines[0]) - 1:
                    l = l + 1
                    break
                l = l + 1
            nbr = lines[index_l][i:i+l]

            x_min = max(index_l-1,0)
            x_max = min(index_l+1,len(lines)-1)
            y_min = max(i-1,0)
            y_max = min(i+l,len(lines[0])-1)

            star_arr = []

            x = x_min
            while x <= x_max:
                y = y_min
                #l_array = []
                while y <= y_max:
                    #print(x, y)
                    #l_array.append(lines[x][y])
                    if not (x == index_l and i <= y <= i + l-1):
                        if lines[x][y] == "*":
                            star_arr.append((x,y))
                            possible_gear_arr.append((int(nbr),(x,y)))
                            pos_arr.append((x,y))
                            #print(lines[x][y])
                            
                    y = y + 1
                #proxy_array.append(l_array)

                x = x + 1




            if len(star_arr) > 0:
                number_arr.append((int(nbr), index_l, i, i+l-1, star_arr))
            i = i + l
        i = i + 1
    index_l = index_l + 1

#print(number_arr)
#print(possible_gear_arr)
#print(pos_arr)
res = 0

while len(pos_arr) > 0:
    gear = pos_arr[0]
    
    if pos_arr.count(gear) == 2:
        res_g = 1
        i = 0
        while i < len(possible_gear_arr):
            if possible_gear_arr[i][1] == gear:
                res_g = res_g * possible_gear_arr[i][0]
                #print(res_g)
            i = i + 1
        res = res + res_g

    while gear in pos_arr:
        pos_arr.remove(gear)
    #print(pos_arr)

print(res)

            








    






 