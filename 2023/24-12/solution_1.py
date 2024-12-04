# import math
# import copy
# import time

def calc_path(hail):
    x_0 = hail[0][0]
    y_0 = hail[0][1]

    v_x = hail[1][0]
    v_y = hail[1][1]

    # coor(t) = v*t + coor_0
    #coor_x(t) = v_x * t + coor_0_x
    #coor_y(t) = v_y * t + coor_0_y
    # path needs to be calculated, replacing t in the system
    # t = (coor_x(t) - coor_0_x) / v_x
    # coor_y(t) = v_y ( coor_x(t) - coor_0_x) / v_x + coor_0_y

    a = v_y / v_x
    b = y_0 - x_0 * a

    return (a, b)

def intersect_x_y(hail1, hail2):
    path1 = calc_path(hail1)
    path2 = calc_path(hail2)

    if path1[0] == path2[0]:
        # parallel path, never cross
        return (False, (0, 0))
    else:
        #not parallel, there is a cross
        # a1 x + b1 = a2 x + b2
        # x = (b2-b1) / (a1 - a2)
        x_target = (path2[1] - path1[1]) / (path1[0] - path2[0]) 
        y_target = path1[0] * x_target + path1[1]
        return (True, (x_target, y_target))

def check_timeline(hail, c_target):
    return (c_target[0] - hail[0][0]) * hail[1][0] >= 0 and (c_target[1] - hail[0][1]) * hail[1][1] >= 0

def full_check(hail1, hail2, interval_min, interval_max):
    intersect_temp = intersect_x_y(hail1, hail2)
    inter_c = intersect_temp[1]
    if not intersect_temp[0]:
        return (False, "Parallel")
    elif not (check_timeline(hail1, inter_c) and check_timeline(hail2, inter_c)):
        return (False, (check_timeline(hail1, inter_c), check_timeline(hail2, inter_c)))
    elif not (interval_min <= inter_c[0] <= interval_max and interval_min <= inter_c[1] <= interval_max):
        return (False, inter_c)
    else:
        return (True, inter_c)



with open('data.txt') as f:
    lines = f.read().splitlines()

#print(lines)

hail_arr = []

for line in lines:
    temp = line.split("@")
    coor_arr_temp = temp[0].split(", ")
    coor_arr = [int(x) for x in coor_arr_temp]

    velocity_arr_temp = temp[1].split(", ")
    velocity_arr = [int(x) for x in velocity_arr_temp]

    hail_arr.append(
        (
            tuple(coor_arr),
            tuple(velocity_arr)
        )
    )

hail_arr_t = tuple(hail_arr)

#print(intersect_x_y(hail_arr_t[0], hail_arr_t[1]))
inter_min = 200000000000000
inter_max = 400000000000000

i = 0
res = 0
while i < len(hail_arr_t) - 1:
    j = i + 1
    while j < len(hail_arr_t):
        f_check_temp = full_check(hail_arr_t[i], hail_arr_t[j], inter_min, inter_max)
        #print(i, j, f_check_temp)
        if f_check_temp[0]:
            res += 1
        j += 1
    i += 1
    print(i)
print(res)

