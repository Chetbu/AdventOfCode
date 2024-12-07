import math
# import copy
# import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")

with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(10 ** math.floor(math.log(1200,10)))
result = 0
#print(lines)
for line in lines:
    temp = line.split(': ')
    expected_result = int(temp[0])
    temp2 = temp[1].split()
    num_arr = [int(x) for x in temp2]
    #print(num_arr)
    possible_outcome = [num_arr[0]]
    i = 1
    while i < len(num_arr):
        new_possible_outcome = []
        #test the number of digits of the right element
        multiplication_factor = 10 ** (math.floor(math.log(num_arr[i],10)) + 1)

        for ele in possible_outcome:
            new_possible_outcome += [ele + num_arr[i], ele * num_arr[i], multiplication_factor* ele + num_arr[i]]
        possible_outcome = new_possible_outcome
        i += 1
    if expected_result in possible_outcome:
        result += expected_result
print(result)