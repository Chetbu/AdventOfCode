import math
# import copy
import time
import functools

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

def bitwise_XOR(a,b):
    #XOR on the number
    f_b = bin(max(a,b))
    s_b = bin(min(a,b))

    #print(f_b, s_b)
    i = -1
    res_b = ""
    while s_b[i] != 'b':
        if f_b[i] != s_b[i] and int(f_b[i]) + int(s_b[i]) == 1:
            res_b = '1' + res_b
        else:
            res_b = '0' + res_b
        i -= 1
    #print(f_b[:i+1])
    res_b = f_b[:i+1] + res_b
    return int(res_b, 2)

#print(bitwise_XOR(42,15))

def prune(n):
    return n % 16777216

#print(prune(100000000))
def calc_next_secret(n):
    secret = n
    first_step = prune(bitwise_XOR(secret * 64, secret))
    secret = first_step
    second_step = prune(bitwise_XOR(int(secret/ 32), secret))
    secret = second_step
    third_step = prune(bitwise_XOR(secret * 2048, secret))
    return third_step

#print(calc_next_secret(123))     

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)

price_list_array = []
price_var_seq_array = []
list_t_seq_arr= []
seq_list = []

for s in [int(x) for x in lines]:
    i = 0
    res_loop = s
    price_list = [s % 10]
    seq = []
    list_tuple_seq = []
    while i < 2000:
        new_res_loop = calc_next_secret(res_loop)
        new_price = new_res_loop % 10

        seq.append(new_price - price_list[-1])
        price_list.append(new_price)
        res_loop = new_res_loop
        if i > 3:
            list_tuple_seq.append(tuple(seq[i-3:]))



        i += 1
    price_list_array.append(tuple(price_list[1:]))
    price_var_seq_array.append(tuple(seq))
    list_t_seq_arr.append(tuple(list_tuple_seq))
    seq_list += list_tuple_seq

print(list_t_seq_arr)
#generate all the possible sequences

# for i in range(-9,10,1):
#     for j in range(-9,10,1):
#         for k in range(-9,10,1):
#             for l in range(-9,10,1):
#                 seq.append((i,j,k,l))

#print(seq)

#run the simulation
max_count = 0

# j = 3
# tes_seq = (0,1,2,3,4)
# print(tes_seq[j-3:j+1], tes_seq[j])

seq_list = list(set(seq_list))

for sequence in seq_list:
    i = 0
    count = 0
    while i < len(price_list_array):
        price_list = price_list_array[i]
        price_var = price_var_seq_array[i]
        list_tuple_seq = list_t_seq_arr[i]

        #go along the seq to see if there is a match
        j = 3
        #print(price_var[j-3:j])
        while price_var[j-3:j+1] != sequence and j < len(price_var):
            j += 1
        if j < len(price_var):
            #sequence found
            #print('sequence found')
            count += price_list[j]
        i += 1

    if count > max_count:
        max_count = count
        print(sequence, max_count)

print(max_count, time.time() - start_time)