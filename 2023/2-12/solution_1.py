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
    indicator = False
    for game in l[1]:
        i = 0
        while i < len(ball_number) and not indicator:
            #print(game)
            if ball_number[i]<game[i]:
                indicator = True
            i = i + 1
        
    if not indicator:
        res_arr.append(l[0])
        res = res + l[0]

#print(res_arr)
print(res)
#print(lines)







    






 