# import math
# import copy
# import time


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
        return coor
    elif True in dir_arr:
        i_true = dir_arr.index(True)
        temp_coor = (
            coor[0] + c_arr[i_true][1][1][0],
            coor[1] + c_arr[i_true][1][1][1]
        )
        return temp_coor
    else:
        return coor

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

def eval_rectangle(n_coor_t:tuple):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for elfe in n_coor_t:
        min_x = min(elfe[0], min_x)
        max_x = max(elfe[0], max_x)
        min_y = min(elfe[1], min_y)
        max_y = max(elfe[1], max_y)
    space_number = (max_y - min_y + 1) * (max_x - min_x + 1) - len(coor_t)
    print("x : ", min_x, max_x, "y : ", min_y, max_y)
    return space_number



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
while round <= 10 :

    new_coor = []
    for elf in coor_t:
        new_coor.append(decide_action(elf,coor_t,cardinal_arr))
    bounce_list = bounce_management(new_coor)
    i = 0
    while i < len(bounce_list):
        new_coor[bounce_list[i]] = coor_t[bounce_list[i]]
        i+=1
    coor_t = tuple(new_coor)
    rotate_cardinal_arr(cardinal_arr)
    round += 1

print(coor_t)
print(eval_rectangle(coor_t))

with open('test_r10.txt') as f:
    lines = f.read().splitlines()

i = 0
coor_arr = []
while i < len(lines):
    j = 0
    while j < len(lines[i]):
        if lines[i][j] == "#":
            coor_arr.append((i ,j ))

        j += 1
    i += 1

coor_t_r1 = tuple(coor_arr)
print(coor_t_r1)
print(eval_rectangle(coor_t_r1))

# for el in coor_t:
#     if not(el in coor_t_r1):
        #print(el)





