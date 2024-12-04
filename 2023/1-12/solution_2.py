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

written_numbers = [
    ["one",1],
    ["two",2],
    ["three",3],
    ["four",4],
    ["five",5],
    ["six",6],
    ["seven",7],
    ["eight",8],
    ["nine",9],
]

res = 0
for word in lines:
    i = 0
    while not word[i].isdigit() and i <= len(word)-1: 
        i = i + 1
    
    if i > len(word)-1:
        value_i = -1
    else:
        value_i = int(word[i])

    
    for w_num in written_numbers:
        if(0 <= word.find(w_num[0])< i):
            i = word.find(w_num[0])
            value_i = w_num[1]
            #print(w_num[0])
    #print([i,value_i] )
    
    j = len(word) - 1
    while not word[j].isdigit() and j >= 0: 
        j = j - 1 

    if j < 0:
        value_j = -1
    else:
        value_j = int(word[j])

    for w_num in written_numbers:
        if(j < word.rfind(w_num[0])< len(word)):
            j = word.rfind(w_num[0])
            value_j = w_num[1]
            #print(w_num[0])
    #print([j,value_j] )

    if value_i == -1:
        print(word)
    
    res = res + 10 * value_i + value_j

print(res)





    






 