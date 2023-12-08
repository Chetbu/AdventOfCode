# import math

def arr_eval(arr):
    return arr.split(",")

#touching cube = 2 similar coord nad a +- 1 deviation

def near_cube_arr(cube:tuple):
    res = [
        (cube[0] + 1,cube[1],cube[2]),
        (cube[0] -1,cube[1],cube[2]),
        (cube[0],cube[1] + 1,cube[2]),
        (cube[0], cube[1] - 1,cube[2]),
        (cube[0],cube[1],cube[2] + 1),
        (cube[0],cube[1],cube[2] - 1)
    ]

    return res

def is_inbound(cube:tuple, limit:tuple):
    res = True
    i = 0
    while res and i < len(cube):
        if  not(0 <= cube[i] <= limit[i]):
            res = False

        i = i + 1
    return res




with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_eval,lines))

    data_arr = []

    for el in lines_array:
        data_arr.append((int(el[0]), int(el[1]), int(el[2])))

    data = tuple(data_arr)

    #print(data)
    # print(near_cube_arr(data[0]))

    
    limit = [-1,-1,-1]
    for el in data:
        i = 0
        while i < len(el):
            limit[i] = max(limit[i], el[i]+2)
            i = i + 1
    
    print(limit)

    
    neg_data = [] #all air cubes

    for a in range(-1,limit[0]):
        for b in range(-1,limit[1]):
            for c in range(-1,limit[2]):
                if not((a,b,c) in data):
                    neg_data.append((a,b,c))

    #print(len(neg_data))

    outside = [(-1,-1,-1)]
    i = 0
    while i < len(outside):
        near_arr = near_cube_arr(outside[i])
        for near_c in near_arr:
            if near_c in neg_data and not(near_c in outside):
                outside.append(near_c)
        i = i + 1

    #print(outside)

    inside = []
    for el in neg_data:
        if not(el in outside):
            inside.append(el)
    
    #print(inside)

    total_open_side = 0
    res = 0

        


    i = 0
    while i < len(data):
        side_arr = near_cube_arr(data[i])
        open_side = 6

        outside_side = 0
        error_arr = []
        for side in side_arr:
            m = 0

            if side in data or side in inside:
                open_side = open_side - 1
                m = m + 1

            if side in outside:
                outside_side = outside_side + 1
                m = m + 1

            if m != 1:
                error_arr.append(side)
            
        res = res + outside_side
        
        
        total_open_side = open_side + total_open_side

        if open_side != outside_side:
            print(data[i], "open side =", open_side, " outside side =", outside_side, "error ", error_arr, "error in data, neg_data, inside and outside ", error_arr[0] in data, error_arr[0] in neg_data, error_arr[0] in inside, error_arr[0] in outside)



        i = i + 1

    print(total_open_side)

    print(res)

    