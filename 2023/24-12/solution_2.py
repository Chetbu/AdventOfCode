# import math
# import copy
# import time

import z3

def par_3d(hail1, hail2):
    v1 = hail1[1]
    v2 = hail2[1]

    i = 0
    para = True
    coef_arr = []
    while i < 3:
        if v2[i] == 0 and v1[i] != 0:
            para = False
        else:
            coef = v1[i] / v2[i]
            coef_arr.append(coef)
        
        i += 1

    if not para:
        return False
    elif len(coef_arr) == 1:
        return True
    else:
        for c in coef_arr:
            if c != coef:
                return False
        return True


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
par_arr = []
i = 0
while i < len(hail_arr_t) - 1:
    j = i + 1
    while j < len(hail_arr_t):
        if par_3d(hail_arr_t[i], hail_arr_t[j]):
            print(hail_arr_t[i], hail_arr_t[j])
            par_arr.append((i,j))

        j += 1
    i += 1

#print(par_arr)

x_0 = z3.Real('x_0')
y_0 = z3.Real('y_0')
z_0 = z3.Real('z_0')

Vx = z3.Real('Vx')
Vy = z3.Real('Vy')
Vz = z3.Real('Vz')


solv = z3.Solver()

#print(solv)

i = 10
i_limit = 13

t_arr = []

for i in range(i_limit):
    t_arr += [z3.Real('t%d' % i)]

i = 0
while i < i_limit:
    h_c = hail_arr_t[i][0]
    h_v = hail_arr_t[i][1]
    solv.add(x_0 + Vx * t_arr[i] == h_c[0] + h_v[0] * t_arr[i])
    solv.add(y_0 + Vy * t_arr[i] == h_c[1] + h_v[1] * t_arr[i])
    solv.add(z_0 + Vz * t_arr[i] == h_c[2] + h_v[2] * t_arr[i])

    i += 1

print(solv)
print(solv.check())
print(solv.model())

print(428589795012222 +196765966839909+261502975177164 )