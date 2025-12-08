
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()



with open(file_filepath) as f:
    lines = f.read().splitlines()

line_arr = [x.split() for x in lines]

grand_total = 0
i = 0
while i < len(line_arr[0]):
    value_array = [int(x[i]) for x in line_arr[:-1]]
    j = 1
    res = value_array[0]
    operand = line_arr[-1][i]
    while j < len(value_array):
        if operand == "*":
            res = res * value_array[j]
        elif operand == "+":
            res += value_array[j]
        j += 1
    grand_total += res
    i += 1

print(grand_total)

