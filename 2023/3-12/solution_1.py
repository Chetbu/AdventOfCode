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

res = 0
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

            #print(nbr)

            x_min = max(index_l-1,0)
            x_max = min(index_l+1,len(lines)-1)
            y_min = max(i-1,0)
            y_max = min(i+l,len(lines[0])-1)

            #print(nbr, x_min, x_max, y_min, y_max)

            detec_symbol = False

            proxy_array = []

            x = x_min
            while x <= x_max:
                y = y_min
                l_array = []
                while y <= y_max:
                    #print(x, y)
                    l_array.append(lines[x][y])
                    if not (x == index_l and i <= y <= i + l-1):
                        if not lines[x][y] == ".":
                            detec_symbol = True
                            #print(lines[x][y])
                            
                    y = y + 1
                proxy_array.append(l_array)

                x = x + 1

            if detec_symbol:
                print(nbr)
                res = res + int(nbr)

            print(proxy_array)


            i = i + l

        i = i + 1
    index_l = index_l + 1

print(res)
    








    






 