# import math
# import copy
# import time

#import operator

def arr_eval(arr, char):
    return arr.split(char)

def result_eval(result):
    if 5 in result:
        #5 of a kind
        return 9
    elif 4 in result:
        return 8
    elif 3 in result and 2 in result:
        return 7
    elif 3 in result:
        return 6
    elif result.count(2) == 4:
        return 5
    elif 2 in result:
        return 4
    elif max(result) == 1:
        return 0
    else:
        print("error")
        return -1


def hand_type(hand:str):
    result = []
    num_j = hand.count("J")
    #print(num_j)
    new_hand = hand
    i = 0

    new_hand = new_hand.replace("A", "Z")
    new_hand = new_hand.replace("K", "Y")
    new_hand = new_hand.replace("Q", "X")
    new_hand = new_hand.replace("J", "0")
    new_hand = new_hand.replace("T", "V")

    while i < len(hand):
        if hand[i] == "J":
            result.append(0)
        else:
            result.append(hand.count(hand[i]))

        i = i + 1
    
    i = 0

    eval_arr = []

    while i < len(result):
        result_j = result.copy()
        k = 0
        while k < len(result):
            if hand[k] == hand[i]:
                result_j[k] = result[i] + num_j
            k = k + 1
        #print(result_j, result_eval(result_j))
        eval_arr.append(result_eval(result_j))
        i = i + 1

    return str(max(eval_arr)) + new_hand
    

with open('data.txt') as f:
    lines = f.read().splitlines()

line_array = []

for line in lines:

    l = line.split(" ")
    line_array.append((hand_type(l[0]), l[0], int(l[1])))

line_array.sort(key=lambda x: x[0])
for line in line_array:
    print(line)

res = 0
i = 0
while i < len(line_array):

    res = res + line_array[i][2] * (i + 1)
    i = i + 1

print(res)



# print(hand_type("AAAAA"))
# print(hand_type("ABAAA"))
# print(hand_type("ABBAA"))
# print(hand_type("AAACD"))
# print(hand_type("ABBAD"))
# print(hand_type("AACBD"))
# print(hand_type("ABCDE"))






    








    






 