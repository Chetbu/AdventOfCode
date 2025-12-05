
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()



with open(file_filepath) as f:
    lines = f.read().splitlines()

index_separation = lines.index('')
# Ca c'est pour toi mon Stéphane !
id_range_array = [(int(y[0]), int(y[1])) for y in [x.split("-") for x in lines[:index_separation]]]

new_id_range_array = [id_range_array[0]]
while len(id_range_array) > 0:
    current_id_range = id_range_array.pop(0)
    # check if any overlap with the range before
    i = 0
    continue_loop = True #to detect if a overlap is seen during the screening
    while i < len(new_id_range_array) and continue_loop:
        r = new_id_range_array[i]

        if not (current_id_range[1] < r[0] or current_id_range[0] > r[1]):
            #overlap detected
            if current_id_range[1] <= r[1] and current_id_range[0] >= r[0]:
                #full overlap with current being smaller, skip the range
                continue_loop = False
            if current_id_range[1] > r[1]:
                #overlap on the end, keep the end and add it to the array of range to test
                new_end_range = (r[1] + 1, current_id_range[1])
                id_range_array.append(new_end_range)
                continue_loop = False
            if current_id_range[0] < r[0]:
                #overlap on the beginning, keep the beginning and add it to the array of range to test
                new_beginning_range = (current_id_range[0], r[0] - 1)
                id_range_array.append(new_beginning_range)
                continue_loop = False
        i += 1
    if continue_loop:
        #if no overlap, add to the result range array
        new_id_range_array.append(current_id_range)
#print(new_id_range_array)
count = 0
for r in new_id_range_array:
    count += r[1] - r[0] + 1
print(count)