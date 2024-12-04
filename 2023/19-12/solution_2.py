# import math
# import copy
# import time




attribute_array = ("x", "m", "a", "s")

def return_workflow(workflow_str, workflow_arr):
    i = 0
    while i < len(workflow_arr):
        if workflow_arr[i][0] == workflow_str:
            return workflow_arr[i]   
        
        i += 1
    


def action_workflow(part_min, part_max, workflow_str, workflow_arr, i_action):
    if workflow_str == "A" or workflow_str == "R":
        action_str = workflow_str
    else:
        workflow = return_workflow(workflow_str, workflow_arr)
    #print(workflow_str, workflow)
        action_str = workflow[1][i_action]

    #print(workflow, action_str)

    if action_str == "A" or action_str == "R":
        #print("end 1")

        return [(action_str, part_min, part_max)]
    elif not ":" in action_str:
        # go to the workflow named by action_str
        #print("tranfert to another workflow 1")
        return action_workflow(part_min, part_max, action_str, workflow_arr, 0)
    else:
        
        action_split_1 = action_str.split(":")
        destination_workflow = action_split_1[1]
        tested_attribute = action_split_1[0][0]
        compare_sign = action_split_1[0][1]
        compare_value = int(action_split_1[0][2:])

        i_attribute = attribute_array.index(tested_attribute)
        part_min_value = part_min[i_attribute]
        part_max_value = part_max[i_attribute]

        if (compare_sign == "<" and part_max_value <= compare_value) or (compare_sign == ">" and part_min_value >= compare_value):
            # go to the next workflow for the full range
            if destination_workflow == "A" or destination_workflow == "R":
                #print("end 1")
                return [(destination_workflow, part_min, part_max)]
            else:
                #print("tranfert to another workflow 2")
                return action_workflow(part_min, part_max, destination_workflow, workflow_arr, 0)
        elif part_min_value < compare_value < part_max_value:
            #split the thing in 2
            if compare_sign == "<":
                split_value = compare_value - 1
                split_part_min = list(part_min)
                split_part_max = list(part_max)
                split_part_min[i_attribute] = split_value + 1
                split_part_max[i_attribute] = split_value
                #print("< split")
                return action_workflow(part_min, tuple(split_part_max), destination_workflow, workflow_arr, 0) + action_workflow(tuple(split_part_min), part_max, workflow_str, workflow_arr, i_action + 1)
            else:
                #print("> split")
                split_value = compare_value + 1
                split_part_min = list(part_min)
                split_part_max = list(part_max)
                split_part_min[i_attribute] = split_value
                split_part_max[i_attribute] = split_value - 1
            return action_workflow(part_min, tuple(split_part_max), workflow_str, workflow_arr, i_action + 1) + action_workflow(tuple(split_part_min), part_max, destination_workflow, workflow_arr, 0)

        else:
            #go to next action of the workflow
            #print("next action")
            return action_workflow(part_min, part_max, workflow_str, workflow_arr, i_action + 1)
        

def calc_possibilities(prod_output):
    prod_min = prod_output[1]
    prod_max = prod_output[2]
    res = 1
    i = 0
    while i < 4:
        res = res * (prod_max[i] - prod_min[i] + 1)
        i += 1
    return res

print("test calc poss", calc_possibilities((0,(1,1,1,1),(4000,4000,4000,4000))))

with open('data.txt') as f:
    lines = f.read().splitlines()


i_separation = lines.index('')

workflow_raw_array = lines[:i_separation]
#part_raw_array = lines[i_separation + 1:]
workflow_arr = []

for raw_workflow in workflow_raw_array:
    s = raw_workflow.split("{")
    workflow_name = s[0]
    action_list = s[1][:-1].split(",")

    workflow_arr.append((workflow_name, tuple(action_list)))

#print(workflow_arr)

part_min = (1,1,1,1)
part_max = (4000, 4000, 4000, 4000)
initial_workflow_str = "in"

res_arr = action_workflow(part_min, part_max, initial_workflow_str, workflow_arr, 0)

#print(res_arr)

final_res = 0
final_denial = 0
for o in res_arr:
    if o[0] == "A":
        final_res += calc_possibilities(o)
    else:
        final_denial += calc_possibilities(o)

print(final_res, final_denial, 4000 ** 4 - final_res - final_denial)

