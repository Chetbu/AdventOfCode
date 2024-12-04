# import math
# import copy
# import time

#import operator

def arr_eval(arr, char):
    return arr.split(char)

colors = [
    "green",
    "blue",
    "red"
]

with open('data.txt') as f:
    lines = f.read().splitlines()

line_array = []
for line in lines:
    eval_1 = arr_eval(line,":")
    eval_2 = arr_eval(eval_1[1],";")
    aggregate_arr = []
    for game in eval_2:
        result_game = arr_eval(game,",")
        #print(result_game)
        tirage_arr = [0, 0, 0]
        for tirage in result_game:
            res_tirage = arr_eval(tirage," ")
            #print(res_tirage)
            i = 0
            while i < len(colors):
                if colors[i] == res_tirage[2]:
                    tirage_arr[i] = int(res_tirage[1])
                i = i + 1
        aggregate_arr.append(tirage_arr)
    line_array.append([int(arr_eval(eval_1[0]," ")[1]),aggregate_arr])

#print(line_array) 

ball_number = [13,14,12]
res_arr = []
res = 0
for l in line_array:
    min_set_cube = [0,0,0]
    for game in l[1]:
        for index in range(len(min_set_cube)):
            min_set_cube[index] = max(min_set_cube[index], game[index])
    #print(min_set_cube)
    power = min_set_cube[0] * min_set_cube[1] * min_set_cube[2]
    #print(power)
    res = res + power

print(res)
            
        





    






 