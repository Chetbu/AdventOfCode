
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

def is_valid_id(id:int):
    id_str = str(id)
    len_id = len(id_str)
    # if len_id % 2 != 0:
    #     return True
    max_len_id = int(len_id / 2)
    # print(f"Checking ID: {id_str} of length {len_id}, max_len_id: {max_len_id}")

    step = 1
    is_valid = True
    while step <= max_len_id and is_valid:
        # is the pattern possible ?
        if len_id % step == 0:
            
            i=step
            pattern = id_str[0:step]
            # print(f"  Testing pattern length: {step} for ID: {id_str}, pattern: {pattern}")
            is_invalid_pattern = True
            while i < len_id and is_invalid_pattern:
                compared_pattern = id_str[i:i+step]
                
                if pattern != compared_pattern:
                    is_invalid_pattern = False
                # print(f"    Comparing pattern: {pattern} with {compared_pattern} at index {i}, is_invalid_pattern: {is_invalid_pattern}")
                i += step
            if is_invalid_pattern:
                is_valid = False

        step += 1
    return is_valid

# test_ids = [1212, 123123, 1234567, 1213, 1231, 111222]
# # test_ids = [1213]
# for ids in test_ids:
#     print(f"ID: {ids} is valid? {is_valid_id(ids)}")
#     # is_valid_id(ids)



with open(file_filepath) as f:
    lines = f.read().splitlines()
    #lines_array = list(map(arr_eval,lines))

#only one line
range_array = [(int(y[0]), int(y[1])) for y in [x.split("-") for x in lines[0].split(",")]]
id_array = []
for r in range_array:
    i = r[0]
    while i <= r[1]:
        id_array.append(i)
        i += 1

score = 0
for id in id_array:
    if not is_valid_id(id):
        # print(f"ID: {id} is invalid")
        score += id
print(score)






    






 