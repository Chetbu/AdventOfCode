
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "test.txt")
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
old_pos = start_pos
count = 0
for line in lines:
    current_pos = next_value(old_pos, split_inputs(line))
    if current_pos >= 100:
        count += current_pos // 100
        new_pos = current_pos % 100
    elif current_pos < 0:
        count += - (current_pos // 100)
        new_pos = current_pos % 100
    else:
        new_pos = current_pos

    # print("old_pos:", old_pos, " current_pos:", current_pos, " new_pos:", new_pos, " count:", count)
    old_pos = new_pos
    

print(count)





    






 