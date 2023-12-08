import math
# import copy
# import time

import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

def arr_eval(arr):
    return arr.split(" ")

def monkey_id_map(i:tuple):
    return i[0]

with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_eval,lines))


monkey_number_array = []
monkey_operation_array = []

for monkey in lines_array:
    monkey_id = monkey[0][:-1]
    if len(monkey) == 2:
        if monkey_id == "humn":
            monkey_human = (monkey_id, int(monkey[1]))
        else:
            monkey_number_array.append((monkey_id, int(monkey[1])))
    else:
        if monkey_id == "root":
            monkey_root = (monkey_id, (monkey[1], "=", monkey[3]))
        else:
            
            monkey_operation_array.append((monkey_id, (monkey[1], monkey[2], monkey[3])))

#print(monkey_number_array)
#print(monkey_operation_array)
count = 0
old_len = len(lines_array)

while len(monkey_operation_array) < old_len and count < 1000:
    old_len = len(monkey_operation_array)
    ope_id = 0
    monkey_id_list = list(map(monkey_id_map,monkey_number_array))
    while ope_id < len(monkey_operation_array):
        try:
            i_m1 = monkey_id_list.index(monkey_operation_array[ope_id][1][0])
            i_m2 = monkey_id_list.index(monkey_operation_array[ope_id][1][2])
            monkey_id = monkey_operation_array[ope_id][0]
            value = ops[monkey_operation_array[ope_id][1][1]](monkey_number_array[i_m1][1],monkey_number_array[i_m2][1])
            #print([monkey_id, value])
            monkey_number_array.append((monkey_id, value))
            del monkey_operation_array[ope_id]


        except:
            pass
        ope_id += 1
    count += 1

#print(count)
#print((monkey_operation_array))

#discover what is the solved side of root
try:
    i_found = monkey_id_list.index(monkey_root[1][0])
    target_value =  monkey_number_array[i_found][1]
    m_found = monkey_root[1][0]
    m_lookup = monkey_root[1][2]
except:
    i_found = monkey_id_list.index(monkey_root[1][2])
    target_value =  monkey_number_array[i_found][1]
    m_found = monkey_root[1][2]
    m_lookup = monkey_root[1][0]

# print(m_found)
# print(target_value)

operation_ref = tuple(monkey_operation_array)
number_ref = tuple(monkey_number_array)

guess = 3059361893900
distance_guess = [0,math.inf]
while 0<= guess < 3059361894000:
    monkey_operation_array = list(operation_ref)
    monkey_number_array = list(number_ref)
    monkey_number_array.append(("humn", guess))
    count = 0


    while len(monkey_operation_array) > 0 and count < 100:
        ope_id = 0
        monkey_id_list = list(map(monkey_id_map,monkey_number_array))
        while ope_id < len(monkey_operation_array):
            try:
                i_m1 = monkey_id_list.index(monkey_operation_array[ope_id][1][0])
                i_m2 = monkey_id_list.index(monkey_operation_array[ope_id][1][2])
                monkey_id = monkey_operation_array[ope_id][0]
                value = ops[monkey_operation_array[ope_id][1][1]](monkey_number_array[i_m1][1],monkey_number_array[i_m2][1])
                #print([monkey_id, value])
                monkey_number_array.append((monkey_id, value))
                del monkey_operation_array[ope_id]


            except:
                pass
            ope_id += 1
        count += 1

    monkey_id_list = list(map(monkey_id_map,monkey_number_array))

    i_target = monkey_id_list.index(m_lookup)
    if monkey_number_array[i_target][1] == target_value:
        print("solution is :", guess)
        guess = -1
    else:
        d = monkey_number_array[i_target][1] - target_value 
        if abs(d) < abs(distance_guess[1]):
            distance_guess = [guess, d]
        guess += 1
print("closest : ", distance_guess)







    






 