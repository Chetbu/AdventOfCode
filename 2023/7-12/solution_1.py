# import math
# import copy
# import time

#import operator

def arr_eval(arr, char):
    return arr.split(char)

def hand_type(hand:str):
    result = []
    new_hand = hand
    i = 0

    new_hand = new_hand.replace("A", "Z")
    new_hand = new_hand.replace("K", "Y")
    new_hand = new_hand.replace("Q", "X")
    new_hand = new_hand.replace("J", "W")
    new_hand = new_hand.replace("T", "V")

    while i < len(hand):
        result.append(hand.count(hand[i]))

        i = i + 1
    
    if 5 in result:
        #5 of a kind
        return "9" + new_hand
    elif 4 in result:
        return "8" + new_hand
    elif 3 in result and 2 in result:
        return "7" + new_hand
    elif 3 in result:
        return "6" + new_hand
    elif result.count(2) == 4:
        return "5" + new_hand
    elif 2 in result:
        return "4" + new_hand
    else:
        return "0" + new_hand

with open('data.txt') as f:
    lines = f.read().splitlines()

line_array = []
for line in lines:

    l = line.split(" ")
    line_array.append((hand_type(l[0]), l[0], int(l[1])))

line_array.sort(key=lambda x: x[0])
print(line_array)

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






    








    






 