# import math
# import copy
# import time

#import operator

def convert_row_numbers(row):
    if not "#" in row:
        return []
    else:
        i = row.find("#")
        r = row + "."
        j = 0
        while r[i + j] == "#":
            j += 1
        return [j] + convert_row_numbers(row[i+j:])


def generate_possible_rows(row):
    res_array = [""]
    i = 0
    while i < len(row):
        if row[i] != "?":
            for j in range(len(res_array)):
                res_array[j] = res_array[j] + row[i]
        else:
            res_array_2 = res_array.copy()
            for j in range(len(res_array)):
                res_array[j] = res_array[j] + "#"
                res_array_2[j] = res_array_2[j] + "."
            res_array = res_array + res_array_2
        i += 1
    return res_array

#print(generate_possible_rows("..??."))

with open('data.txt') as f:
    lines = f.read().splitlines()

line_array = []
for line in lines:
    l = line.split(" ")
    l_nbr = l[1].split(",")
    arr = []
    for n in l_nbr:
        arr.append(int(n))

    line_array.append(
        (l[0], tuple(arr))
    )
#print(line_array)

#print(convert_row_numbers(".#.###.#.######"))
res = 0
for line in line_array:
    count = 0
    row = line[0]
    possible_arr = generate_possible_rows(row)
    for pos_row in possible_arr:
        eval = convert_row_numbers(pos_row)
        if line[1] == tuple(eval):
            count += 1
    res += count
    
    #print(count)

print(res)






 