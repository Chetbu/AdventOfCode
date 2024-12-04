# import math
# import copy
# import time
import re

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)

file_filepath = Path(current_dir, "data.txt")

with open(file_filepath) as f:
    string = f.read()


#print(string)

pattern = r'(mul\(\d*,\d*\))|(do\(\))|(don\'t\(\))'
#pattern = r'do\(\)'

all_mul_arr = re.findall(pattern,string)
#print(all_mul_arr)

enable = True
res = 0
for item_arr in all_mul_arr:
    item = item_arr[0]
    if item == '':
        if item_arr[2] == '':
            enable = True
        else:
            enable = False
    if enable and item != '':
        split_item = item[4:-1].split(',')
        res += int(split_item[0]) * int(split_item[1])

print(res)