
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()




with open(file_filepath) as f:
    lines = f.read().splitlines()
    #lines_array = list(map(arr_eval,lines))

sum_joltage = 0
for line in lines:
    i = 0
    i_0 = 0
    max_0 = 0
    while i < len(line) - 1:
        if int(line[i]) > max_0:
            i_0 = i
            max_0 = int(line[i])
        i += 1
    # print("Max i is ", max_0, " at ", i_0)
    j = i_0 + 1
    j_0 = j
    max_1 = 0
    while j < len(line):
        if int(line[j]) > max_1:
            j_0 = j
            max_1 = int(line[j])
        j += 1
    # print("Max j is ", max_1, " at ", j_0)
    value = int(max_0) * 10 + int(max_1)
    #print("value found is ", value, "for i_0, j_0 ", (max_0, max_1))
    sum_joltage += value

print(sum_joltage)






    






 