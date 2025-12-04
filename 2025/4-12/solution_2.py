import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

possible_moves_array = []
for i in range(-1,2,1):
    for j in range(-1,2,1):
        possible_moves_array.append((i,j))
possible_moves_array.remove((0,0))
# print(possible_moves_array)

def count_adjacent_rolls(t, map):
    count = 0
    for m in possible_moves_array:
        new_t = (t[0] + m[0], t[1] + m[1])
        if new_t[0] < 0 or new_t[1] < 0 or new_t[0] >= len(map) or new_t[1] >= len(map[0]):
            #coordonate outside the map, considered as a space
            continue
        elif map[new_t[0]][new_t[1]] == "@":
            count += 1
    return count



with open(file_filepath) as f:
    lines = f.read().splitlines()

total_result = 0
result = 1
current_map = lines

while result > 0:
    result = 0
    new_map = current_map.copy()
    i = 0
    while i < len(current_map):
        j = 0
        while j < len(current_map[i]):
            if current_map[i][j] == "@":
                count = count_adjacent_rolls((i,j),current_map)
                if count <= 3:
                    result += 1
                    new_map[i] = new_map[i][:j] + "." + new_map[i][j+1:]
            j += 1
        i += 1
    current_map = new_map
    total_result += result
print(total_result)