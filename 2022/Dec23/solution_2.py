# import math
# import copy
import time


# def arr_eval(arr):
#     return arr.split(" ")

cardinal_arr = [
    ("N", ((-1,-1), (-1,0), (-1,1))),
    ("S", ((1,-1), (1,0), (1,1))),
    ("W",  ((-1,-1), (0,-1), (1,-1))),
    ("E", ((-1,1), (0,1), (1,1)))
    ]

def rotate_cardinal_arr(c_arr:list):
    c_arr.append(c_arr[0])
    del c_arr[0]

def scan(coor:tuple, coor_arr:tuple, c_arr:list):
    i = 0
    dir_arr = []
    while i < len(c_arr):
        j = 0
        empty_dir = True
        while j < len(c_arr[i][1]) and empty_dir:
            temp_coor = (
                coor[0] + c_arr[i][1][j][0],
                coor[1] + c_arr[i][1][j][1]
            )
            
            if temp_coor in coor_arr: #if an elf near in this orientation
                #print(temp_coor, i)
                empty_dir = False

            j+=1
        dir_arr.append(empty_dir)
        i+=1
    return dir_arr

def decide_action(coor:tuple, coor_arr:tuple, c_arr:list):
    dir_arr = scan(coor, coor_arr, c_arr)
    if not(False in dir_arr): #if nothing near the elf, does nothing
        return (coor, False)
    elif True in dir_arr:
        i_true = dir_arr.index(True)
        temp_coor = (
            coor[0] + c_arr[i_true][1][1][0],
            coor[1] + c_arr[i_true][1][1][1]
        )
        return (temp_coor, True)
    else:
        return (coor, False)

def bounce_management(n_coor_arr:list):
    i = 0
    bounce_list = []
    while i < len(n_coor_arr):
        count = n_coor_arr.count(n_coor_arr[i])
        if count == 2:
            #generate list of index of duplicate / only 2 can append by design
            bounce_list.append(i)

        elif count > 2: #error management
            return ValueError("more than 2 elf colliding")

        i+=1
    return bounce_list



with open('data.txt') as f:
    lines = f.read().splitlines()

i = 0
coor_arr = []
while i < len(lines):
    j = 0
    while j < len(lines[i]):
        if lines[i][j] == "#":
            coor_arr.append((i,j))

        j += 1
    i += 1

coor_t = tuple(coor_arr)

round = 1
stop_value = True
st = time.time()
it = time.time()

while round <= 10000 and stop_value :

    new_coor = []
    has_moved = []
    for elf in coor_t:
        next_action = decide_action(elf,coor_t,cardinal_arr)
        new_coor.append(next_action[0])
        has_moved.append(next_action[1])
    bounce_list = bounce_management(new_coor)
    i = 0
    while i < len(bounce_list):
        new_coor[bounce_list[i]] = coor_t[bounce_list[i]]
        i+=1
    coor_t = tuple(new_coor)
    rotate_cardinal_arr(cardinal_arr)
    if True in has_moved:
        round += 1
        if round % 10 == 0:
            
            print("round :",round, "number of moves :", has_moved.count(True), "10r time :", it - st, "Total time :", time.time() - st)
            it = time.time()

    else:
        print("end round: ", round, "Total time :", time.time() - st)
        stop_value = False

#print(coor_t)






