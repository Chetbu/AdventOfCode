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


def pattern_transpose(pattern):
    new_pattern = []
    for j in range(len(pattern[0])):
        s = ""
        for i in range(len(pattern)):
            s += pattern[i][j]
        new_pattern.append(s)
    return new_pattern


print(line_symetry(['#...##..#', '#....#..#', '..##..###', '#####.##.', '#####.##.', '..##..###', '#....#..#']))
print(line_symetry(['#.##..##.', '..#.##.#.', '##......#', '##......#', '..#.##.#.', '..##..##.', '#.#.##.#.']))
print(line_symetry(pattern_transpose(['#.##..##.', '..#.##.#.', '##......#', '##......#', '..#.##.#.', '..##..##.', '#.#.##.#.'])))


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
    l_sym = line_symetry(pattern)
    if l_sym[0]:
        res = res + 100 *l_sym[1]
    else:
        l_v_sym = line_symetry(pattern_transpose(pattern))
        if not l_v_sym:
            print("no symetry")
        res = res + l_v_sym[1]

print(res)


    




 