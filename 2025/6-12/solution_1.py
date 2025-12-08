
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()



with open(file_filepath) as f:
    lines = f.read().splitlines()

#Pour toi mon Burg
screening_array = [x == "S" for x in lines[0]]
i = 1
count = 0
while i < len(lines):
    new_screening_array = screening_array
    for j, val in enumerate(lines[i]):
        if screening_array[j] and val == "^":
            count += 1
            new_screening_array[j-1] = True
            new_screening_array[j] = False
            new_screening_array[j + 1 ] = True
    screening_array = new_screening_array
    # print(sum(screening_array))
    i += 1
print(count)

