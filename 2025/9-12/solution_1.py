import math
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()



with open(file_filepath) as f:
    lines = f.read().splitlines()

coord_array = [(int(x[0]), int(x[1])) for x in [y.split(',') for y in lines]]
# print(coord_array)

i = 0
max_area = 0
while i < len(coord_array) - 1:
    j = i + 1
    while j < len(coord_array):
        #calc the area of the rectangle
        c1 = coord_array[i]
        c2 = coord_array[j]
        area = abs(c1[0] - c2[0] + 1) * abs(c1[1] - c2[1] + 1)
        if area > max_area:
            max_area = area
            # print(f"New max area {max_area} between {c1} and {c2}")


        j += 1
    i += 1

print(f"Max area is {max_area}")



 