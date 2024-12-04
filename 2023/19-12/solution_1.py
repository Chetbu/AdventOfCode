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
    


def action_workflow(part, workflow_str, workflow_arr, i_action):
    workflow = return_workflow(workflow_str, workflow_arr)
    action_str = workflow[1][i_action]

    #print(workflow, action_str)

    if action_str == "A" or action_str == "R":

        return action_str
    elif not ":" in action_str:
        # go to the workflow named by action_str
        return action_workflow(part, action_str, workflow_arr, 0)
    else:
        
        action_split_1 = action_str.split(":")
        destination_workflow = action_split_1[1]
        tested_attribute = action_split_1[0][0]
        compare_sign = action_split_1[0][1]
        compare_value = int(action_split_1[0][2:])

        i_attribute = attribute_array.index(tested_attribute)
        part_value = part[i_attribute]

        if (compare_sign == "<" and part_value < compare_value) or (compare_sign == ">" and part_value > compare_value):
            # go to the next workflow
            if destination_workflow == "A" or destination_workflow == "R":
                return destination_workflow
            else:
                return action_workflow(part, destination_workflow, workflow_arr, 0)
        else:
            #go to next action of the workflow
            return action_workflow(part, workflow_str, workflow_arr, i_action + 1)
        



with open('data.txt') as f:
    lines = f.read().splitlines()


i_separation = lines.index('')

workflow_raw_array = lines[:i_separation]
part_raw_array = lines[i_separation + 1:]
workflow_arr = []

for raw_workflow in workflow_raw_array:
    s = raw_workflow.split("{")
    workflow_name = s[0]
    action_list = s[1][:-1].split(",")

    workflow_arr.append((workflow_name, tuple(action_list)))

#print(workflow_arr)

part_arr = []
for r_part in part_raw_array:
    arr = r_part[1:-1].split(",")
    v_arr = [0,0,0,0]
    for a in arr:
        temp = a.split("=")
        i = attribute_array.index(temp[0])
        v_arr[i] = int(temp[1])
    part_arr.append(tuple(v_arr))

#print(part_arr)
res = 0  
for part in part_arr:
    initial_workflow_str = "in"
    end_str = action_workflow(part, initial_workflow_str, workflow_arr, 0)
    if end_str == "A":
        for c in part:
            res += c
    
print(res)