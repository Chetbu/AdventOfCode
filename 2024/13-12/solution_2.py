import math
# import copy
import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()



with open(file_filepath) as f:
    lines = f.read().splitlines()

#print(lines)
i = 0
machine_arr = []
current_machine = []
while i < len(lines):
    if len(lines[i]) == 0:
        machine_arr.append(current_machine)
        current_machine = []
    else:
        s = lines[i]
        replacement = (': ', '+', '=',', ')
        for r in replacement:
            s = s.replace(r, '_')
        s_arr = s.split('_')
        current_machine.append((int(s_arr[2]), int((s_arr[4]))))

    i += 1
machine_arr.append(current_machine)
#print(machine_arr)

#check if a machine as a 0 in one of the tuple and change the last tuple for solution 2
has_zero = False
add_factor = 10000000000000
for m in machine_arr:
    for t in m:
        if 0 in t:
            has_zero = True
    m[2] = (m[2][0] + 10000000000000, m[2][1] + 10000000000000)
print("Any zero detected in the data ?", has_zero)
#print('test int', int(0.9999999999999))
total_token = 0
#for each machine, let's calculate the number of time
for m in machine_arr:
    
    delta = (m[1][1] * m[0][0] - m[0][1] * m[1][0])
    #print(delta)
    #if delta not 0, there is at only one solution
    if delta != 0:
        nbr_push_a = (m[2][0] - m[2][1]*m[1][0]/m[1][1]) * m[1][1] / delta

        #print(nbr_push_a)
        nbr_push_b = (m[2][0] - nbr_push_a * m[0][0]) / m[1][0]
        #print(nbr_push_b)

        #create the next integer before and after the nbr of push, and test if a solution exist
        if nbr_push_a >= 0 and nbr_push_b >= 0:
            possible_solution_arr = []
            for offset_a in [0,1]:
                for offset_b in [0,1]:
                    round_a = int(math.floor(nbr_push_a)) + offset_a
                    round_b = int(math.floor(nbr_push_b)) + offset_b
                    #print(round_a,round_b)
                    r_x = round_a* m[0][0] + round_b* m[1][0]
                    r_y = round_a* m[0][1] + round_b* m[1][1]
                    if r_x == m[2][0] and r_y == m[2][1]:
                        possible_solution_arr.append((int(math.floor(nbr_push_a)) + offset_a, int(math.floor(nbr_push_b)) + offset_b))
            #print(possible_solution_arr)

            if len(possible_solution_arr) !=0:
                #print(possible_solution_arr)
                nbr_token = 3* possible_solution_arr[0][0] + possible_solution_arr[0][1]
                #print(nbr_token)
                total_token += nbr_token
            # else:
            #     print((nbr_push_a, nbr_push_b), (round_a, round_b))

    else:
        print("Delta = 0", m)

print(total_token)