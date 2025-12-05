
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
ingredients_array = [int(x) for x in lines[index_separation + 1:]]

# print(id_range_array, ingredients_array)
count = 0

for ingredient in ingredients_array:
    is_fresh = False
    i = 0
    while i < len(id_range_array) and not is_fresh:
        range = id_range_array[i]
        if range[0] <= ingredient <= range[1]:
            is_fresh = True
        if is_fresh:
            count += 1
        i += 1

print(count)
    






 