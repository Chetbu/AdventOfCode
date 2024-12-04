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

pattern = r'mul\(\d*,\d*\)'

all_mul_arr = re.findall(pattern,string)
#print(x)

res = 0
for item in all_mul_arr:
    split_item = item[4:-1].split(',')
    res += int(split_item[0]) * int(split_item[1])

print(res)
 