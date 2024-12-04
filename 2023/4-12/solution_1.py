# import math
# import copy
# import time

#import operator

def arr_eval(arr, char):
    return arr.split(char)


with open('data.txt') as f:
    lines = f.read().splitlines()

line_array = []
res = 0
for line in lines:
    eval_1 = arr_eval(line,":")
    eval_2 = arr_eval(eval_1[1],"|")

    #print(eval_1)
    #print(eval_2)
    aggregate_arr = []
    for member in eval_2:
        eval_3 = arr_eval(member," ")
        while '' in eval_3:
            eval_3.remove('')
        nbr_arr = []
        for element in eval_3:
            nbr_arr.append(int(element))
        aggregate_arr.append(nbr_arr)
    #print(aggregate_arr)

    score = 0

    for element in aggregate_arr[0]:
        if element in aggregate_arr[1]:
            score = score + 1
    
    if score > 0:
        res = res + 2 ** (score-1)

print(res)


    








    






 