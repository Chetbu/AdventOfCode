# import math
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
        monkey_number_array.append((monkey_id, int(monkey[1])))
    else:
        monkey_operation_array.append((monkey_id, (monkey[1], monkey[2], monkey[3])))

#print(monkey_number_array)
#print(monkey_operation_array)
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

print(len(monkey_operation_array))
monkey_id_list = list(map(monkey_id_map,monkey_number_array))
i_root = monkey_id_list.index("root")
print(monkey_number_array[i_root][1])






    






 