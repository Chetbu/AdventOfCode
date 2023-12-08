# import math
import copy
import time

def move_value_in_array(i:int, ref_arr:tuple, arr:list, index_arr:list):
    val = ref_arr[i] #value to move
    val_arr_index = index_arr.index(i) #index stored in the index array

    abs_target_i = val_arr_index + val
    if abs_target_i < 0:
        target_i = (abs_target_i + (abs_target_i // len(arr))) % len(arr)

    elif abs_target_i > len(arr):
        target_i = (abs_target_i  + (abs_target_i // len(arr))) % len(arr)
    else:
        target_i = abs_target_i
    #print(val, target_i)

    del arr[val_arr_index]
    arr.insert(target_i, val)

    del index_arr[val_arr_index]
    index_arr.insert(target_i, i)


    return


with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(int,lines))

ref_array = tuple(lines_array)

index_array = list(range(0,len(ref_array)))
#print(index_array)

#print(lines_array[0])

#print(lines_array)

i = 0 #generate the final arr
while i < len(ref_array):
    move_value_in_array(i, ref_array, lines_array, index_array)
    #print(lines_array)    
    i += 1

i_0 = lines_array.index(0) #look for 0 in the array
i = 1
sum = 0
while i < 4:
    index = i_0 + i * 1000
    j = index % len(lines_array)
    print(lines_array[j])
    sum = sum + lines_array[j]
    i +=1

print("sum :", sum)



    






 