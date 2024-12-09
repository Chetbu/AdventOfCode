# import math
# import copy
# import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")



with open(file_filepath) as f:
    lines = f.read().splitlines()

id = 0
HDD_list = []

i = 0
while i < len(lines[0]):
    longueur_segment = int(lines[0][i])
    if i % 2 == 0:
        #is a data block
        HDD_list += [id] * longueur_segment
        id += 1
    else:
        HDD_list += ['.'] * longueur_segment
    i += 1

#print(HDD_list)

#move the blocks from end to beginning

i = 0
j = len(HDD_list) -1 

while i < j:
    #search for the next empty element
    while HDD_list[i] != '.' and i<j:
        i += 1
    #search for the last non empty element
    while HDD_list[j] == '.' and i <j:
        j -= 1
    #swap the element
    HDD_list[i] = HDD_list[j]
    HDD_list[j] = '.'

#print(HDD_list)

#calc checksum

i = 0
check_sum = 0
while i < len(HDD_list) and HDD_list[i] != '.':
    check_sum += i * HDD_list[i]
    i += 1

print(check_sum)