
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

def split_inputs(line):
    dir = line[0]
    val = int(line[1:])
    if dir == "L":
        dir_v = -1
    else:
        dir_v = 1
    return (dir_v, val)

def next_value(curr_pos, move):
    return curr_pos + move[0]* move[1]

with open(file_filepath) as f:
    lines = f.read().splitlines()
    #lines_array = list(map(arr_eval,lines))

start_pos = 50
solution_arr = [start_pos]
count_arr = [0]
count = 0
for line in lines:
    current_pos = next_value(solution_arr[-1], split_inputs(line))
    if solution_arr[-1] == 0 and current_pos < 0:
        current_pos += 100

    calculated_pos = current_pos
    current_count = 0
    while current_pos < 0 or current_pos > 100:
        if current_pos < 0:
            current_pos += 100
            current_count += 1
            count += 1
        elif current_pos >= 100:
            current_pos -= 100
            count += 1
            current_count += 1
    if current_pos == 0 or current_pos == 100:
        current_pos = 0
        current_count += 1
        count += 1
    # print("start pos :", solution_arr[-1], " calculated pos:", calculated_pos, " final pos:", current_pos, " count:", current_count)

    solution_arr.append(current_pos)
    count_arr.append(count)
    
 
# print(solution_arr)
# print(count_arr)
print(count)





    






 