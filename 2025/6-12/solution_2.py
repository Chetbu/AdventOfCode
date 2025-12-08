
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()



with open(file_filepath) as f:
    lines = f.read().splitlines()

#Pour toi mon Burg
screening_array = [(x == "S") * 1 for x in lines[0]]
i = 1
while i < len(lines):
    new_screening_array = screening_array
    for j, val in enumerate(lines[i]):
        if screening_array[j] > 0 and val == "^":
            new_screening_array[j-1] += screening_array[j]
            new_screening_array[j+1] += screening_array[j]
            new_screening_array[j] = 0
    # screening_array = new_screening_array
    # print(screening_array)
    i += 1
print(sum(screening_array))
