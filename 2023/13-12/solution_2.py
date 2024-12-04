# import math
# import copy
# import time

#import operator

#print(generate_possible_rows("..??."))

def line_symetry(pattern):
    i = 1
    symetry = False
    while i < len(pattern):
        symetry = False
        if pattern[i - 1] == pattern [i]:
            #print("first symetrie", i)
            symetry = True
            j = 1
            while (i - j - 1) >= 0 and i + j < len(pattern) and symetry:
                if pattern[i - 1 - j] != pattern [i + j]:
                    symetry = False
                j += 1
            
        if symetry:
            
            break

        i += 1
    return (symetry, i)

def nbr_difference_row(row1, row2):
    count = 0
    for i in range(len(row1)):
        if row1[i] != row2[i]:
            count += 1
    return count


def line_near_symetry(pattern):
    i = 1
    res = []
    while i < len(pattern):

        symetry_false_arr = []
        j = 0
        while (i - j - 1) >= 0 and i + j < len(pattern) and len(symetry_false_arr) <=1:
            if pattern[i - 1 - j] != pattern [i + j]:

                count_diff_row = nbr_difference_row(pattern[i - 1 - j], pattern [i + j])
                symetry_false_arr.append(
                    (j, count_diff_row)
                )
            j += 1
            
        if len(symetry_false_arr) == 1:
            if symetry_false_arr[0][1] == 1:
                return (True, i)

        i += 1
    return (False, i)


def pattern_transpose(pattern):
    new_pattern = []
    for j in range(len(pattern[0])):
        s = ""
        for i in range(len(pattern)):
            s += pattern[i][j]
        new_pattern.append(s)
    return new_pattern


#print(line_symetry(['#...##..#', '#....#..#', '..##..###', '#####.##.', '#####.##.', '..##..###', '#....#..#']))
#print(line_symetry(['#.##..##.', '..#.##.#.', '##......#', '##......#', '..#.##.#.', '..##..##.', '#.#.##.#.']))
#print(line_symetry(pattern_transpose(['#.##..##.', '..#.##.#.', '##......#', '##......#', '..#.##.#.', '..##..##.', '#.#.##.#.'])))

#print(line_near_symetry(['#...##..#', '#....#..#', '..##..###', '#####.##.', '#####.##.', '..##..###', '#....#..#']))
#print(line_near_symetry(['#.##..##.', '..#.##.#.', '##......#', '##......#', '..#.##.#.', '..##..##.', '#.#.##.#.']))
#print(nbr_difference_row("....",".##."))

#print(pattern_transpose(['#.##..##.', '..#.##.#.', '##......#', '##......#', '..#.##.#.', '..##..##.', '#.#.##.#.']))

with open('data.txt') as f:
    lines = f.read().splitlines()

#print(lines)

pat_array = []

while "" in lines:
    i = lines.index("")
    m = lines[:i]
    pat_array.append(m)
    lines = lines[i+1:]

pat_array.append(lines)
#print(pat_array)

res = 0
for pattern in pat_array:
    l_sym = line_near_symetry(pattern)
    if l_sym[0]:
        res = res + 100 *l_sym[1]
    else:
        l_v_sym = line_near_symetry(pattern_transpose(pattern))
        if not l_v_sym:
            print("no symetry")
        res = res + l_v_sym[1]

print(res)


    




 