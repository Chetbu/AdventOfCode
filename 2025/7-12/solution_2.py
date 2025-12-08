
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()



with open(file_filepath) as f:
    lines = f.read().splitlines()

# print(lines)
#spot the empty column for split
i_0 = 0
i = 1
grd_result = 0
while i < len(lines[0]) + 1:
    if i == len(lines[0]) or len(set([x[i] for x in lines])) == 1:
        #column empty, data is between i and i_0
        j = i_0
        operand = lines[-1][i_0]
        if operand == "*":
            calc = 1
        else:
            calc = 0
        while j < i:
            res_str = ''
            for line in lines[:-1]:
                if line[j] != " ":
                    res_str += line[j]

            j += 1
            if operand == "*":
                calc = calc * int(res_str)
            elif operand == "+":
                calc += int(res_str)
        grd_result += calc
        i_0 = j + 1
    i += 1

print(grd_result)


