# import math
import copy
# import time

dir_inc_arr_t = ((1,0,0), (0,1,0), (0,0,1))

def expand_brick(coor_c):
    #return a tupple containing all the occupied space of the brick
    i = 0
    #map the changing coor
    while i < 3 and coor_c[0][i] == coor_c[1][i]:
        i += 1
    if i == 3:
        #only one block, return and tupple of one element
        return (coor_c[0] ,)
    else:

        temp_l = list(coor_c)
        temp_l.sort(key=lambda tup: tup[i])
        new_coor = list(temp_l[0])
        res = [temp_l[0]]
        j = 1
        while j <= temp_l[1][i] - temp_l[0][i]:
            new_coor[i] = new_coor[i] + 1
            res.append(tuple(new_coor))
            j+=1
        return tuple(res)

def brick_fall(ex_brick, z):
    res = []
    for cube in ex_brick:
        temp = list(cube)
        temp[2] = temp[2] - z
        res.append(tuple(temp))
    return tuple(res)

#print(expand_brick(((2, 2, 339), (2, 2, 348))))   

# def brick_fall(coor_c, z_fall, occupied_space_a):


def critical_bricks_index_arr(supporting_arr_f):
    count = 0

    supporting_brick_index_arr = []

    i = 0
    while i < len(supporting_arr_f):
        if supporting_arr_f[i] == []:
            count += 1
        else:
            temp_element_are_supported = []
            
            for ele in supporting_arr_f[i]:
                j = 0
                is_supported_by_other_brick = False
                while j < len(supporting_arr_f):
                    if i != j:
                        if ele in supporting_arr_f[j]:
                            is_supported_by_other_brick = True
                            #print(i, ele, j)
                    j += 1
                temp_element_are_supported.append(is_supported_by_other_brick)
            
            #print(temp_element_are_supported)
            if not False in temp_element_are_supported:
                #print("ping")
                count += 1
            else:
                supporting_brick_index_arr.append(i)



            #print(temp_element_are_supported, count)

        i += 1

    #print(count)
    return (count, supporting_brick_index_arr)

with open('data.txt') as f:
    lines = f.read().splitlines()

#print(lines)

coor_arr = []

for line in lines:
    s = line.split("~")
    coor_couple = []
    for ele in s:
        temp = ele.split(",")
        coor = (int(temp[0]), int(temp[1]), int(temp[2]))
        coor_couple.append(coor)
    coor_couple.sort(key=lambda tup: tup[2])
    coor_arr.append(tuple(coor_couple))

coor_arr.sort(key=lambda tup: tup[0][2])
coor_arr_t = tuple(coor_arr)
#print(coor_arr_t)

#create a table expanding all the bricks
brick_falling_arr = []
for c in coor_arr_t:
    brick_falling_arr.append(expand_brick(c))
#print(brick_falling_arr)
landed_state_dict = dict()
landed_on_brick_dict = dict()

index_brick = 0
for brick in brick_falling_arr:
    #make bricks fall one by one
    current_brick = brick

    landed = False
    landed_on_arr = []
    while not landed:
        fallen_brick = brick_fall(current_brick, 1)

        for cube in fallen_brick:
            if cube in landed_state_dict:
                landed = True
                landed_on_arr.append(landed_state_dict[cube])
            elif cube[2] == 0:
                landed = True
        
        if landed:
            for cube in current_brick:

                landed_state_dict[cube] = index_brick
        else:
            current_brick = fallen_brick
    
    landed_on_brick_dict[index_brick] = list(dict.fromkeys(landed_on_arr))

    index_brick += 1

landed_on_list_v = list(landed_on_brick_dict.values()) 
print(landed_on_list_v)

filter_landed_on_only_one = [x[0] for x in landed_on_list_v if len(x) == 1]
print(len(coor_arr) - len(dict.fromkeys(filter_landed_on_only_one)))

i = 0
supporting_arr = []
while i < len(landed_on_list_v):
    temp = []
    j = 0
    while j < len(landed_on_list_v):
        if i in landed_on_list_v[j]:
            temp.append(j)
        j += 1
    supporting_arr.append(temp)
    i += 1

#print(supporting_arr)

temp_res = critical_bricks_index_arr(supporting_arr)
supporting_brick_index_arr = temp_res[1]
print(temp_res[0])


print(supporting_brick_index_arr)
res = 0
for sup_index in supporting_brick_index_arr:
    chain_reac_arr = copy.deepcopy(landed_on_list_v)
    disp_brick_arr = [sup_index]
    i = 0
    while i < len(disp_brick_arr):
        current_ind = disp_brick_arr[i]
        j = 0
        while j < len(chain_reac_arr):
            if current_ind in chain_reac_arr[j]:
                chain_reac_arr[j].remove(current_ind)
                if len(chain_reac_arr[j]) == 0:
                    disp_brick_arr.append(j)
            j += 1
        
        i += 1

    #print(disp_brick_arr)
    res = len(disp_brick_arr) - 1 + res

print(res)







