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




with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_eval,lines))

    data = []

    for el in lines_array:
        data.append((int(el[0]), int(el[1]), int(el[2])))

    # print(data)
    # print(near_cube_arr(data[0]))

    total_open_side = 0

    i = 0
    while i < len(data):
        side_arr = near_cube_arr(data[i])
        open_side = 6
        for side in side_arr:
            if side in data:
                open_side = open_side - 1
            
        total_open_side = open_side + total_open_side

        i = i + 1

    print(total_open_side)

    