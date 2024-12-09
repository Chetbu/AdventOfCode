# import math
# import copy
import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()


with open(file_filepath) as f:
    lines = f.read().splitlines()

id = 0
HDD_list = []

i = 0
while i < len(lines[0]):
    longueur_segment = int(lines[0][i])
    if i % 2 == 0:
        #is a data block
        HDD_list += [(id, longueur_segment)]
        id += 1
    else:
        HDD_list += [('.', longueur_segment)]
    i += 1

print(HDD_list)

#move the blocks from end to beginning

i = 0
j = len(HDD_list) - 1
#print(HDD_list[j][0])

while j >= 0:
    #take the next data block
    #print(j)
    while HDD_list[j][0] == '.':
        j -= 1
    data_len = HDD_list[j][1]
    
    #search for an empty space large enough
    i = 0
    while (HDD_list[i][0] != '.' or HDD_list[i][1] < data_len) and i < j:
        i += 1
    
    if i >= j:
        #no space found, can't move, switch to next one
        j -= 1
    else:
        #switch
        remaining_space_after_move = HDD_list[i][1] - data_len

        #switch the data
        HDD_list[i] = HDD_list[j]
        HDD_list[j] = ('.', HDD_list[i][1])
        if remaining_space_after_move > 0:
            #add empty space
            HDD_list.insert(i+1,('.',remaining_space_after_move))
            j += 1

#print(HDD_list)

#calc checksum

i = 0
index_HDD = 0
check_sum = 0
while i < len(HDD_list):
    if HDD_list[i][0] == '.':
        id_file_checksum = 0
    else:
        id_file_checksum = HDD_list[i][0]
    j = 0
    while j < HDD_list[i][1]:
        check_sum += id_file_checksum * index_HDD
        index_HDD += 1
        j += 1
    i += 1


print(check_sum, time.time() - start_time)