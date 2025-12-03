
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()




with open(file_filepath) as f:
    lines = f.read().splitlines()
    #lines_array = list(map(arr_eval,lines))

int_lines : list[list[int]]= []
for line in lines:
    int_array = [int(x) for x in line]
    int_lines.append(int_array)


sum_joltage = 0
max_figures = 12

for line in int_lines:
    line_joltage = 0
    f = 0
    i_last_iteration = -1
    while f < max_figures:
        i = i_last_iteration + 1
        i_0 = 0
        max_0 = 0
        # debug_array = []
        while i < len(line) - max_figures + 1 + f:
            # debug_array.append(line[i])
            if line[i] > max_0:
                i_0 = i
                max_0 = line[i]
            i += 1
        # print("Max i is ", max_0, " at ", i_0, " for f ", f, "Debug array ", debug_array)
        i_last_iteration = i_0
        line_joltage = 10 * line_joltage + max_0
        f += 1
    # print(line_joltage)
    sum_joltage += line_joltage
print(sum_joltage)






    






 