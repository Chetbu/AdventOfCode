# import math
# import copy
# import time

#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)

def check_is_in_order(ordering_rule_list, first_page,second_page):
    return [first_page, second_page] in ordering_rule_list

def check_update(ordering_rule_list, update):
    current_page_index = 0
    res = True
    while res and current_page_index < len(update) - 1:
        compared_page_index = current_page_index + 1
        res_page = True
        while compared_page_index < len(update) and res_page:
            res_page = check_is_in_order(ordering_rule_list, update[current_page_index], update[compared_page_index])
            compared_page_index += 1
        res = res_page
        current_page_index += 1
    return res

file_filepath = Path(current_dir, "data.txt")

with open(file_filepath) as f:
    lines = f.read().splitlines()

index_split = lines.index('')
# print(index_split)
# print(lines[:index_split])
# print(lines[index_split + 1:])

ordering_rule_list_temp = [x.split('|')  for x in lines[:index_split]]
ordering_rule_list = []
for rules in ordering_rule_list_temp:
    res_rule = []
    for ele in rules:
        res_rule.append(int(ele))
    ordering_rule_list.append(res_rule)

#print(ordering_rule_list)
page_number_list = []
for ele in [x.split(',')  for x in lines[index_split+1:]]:
    res_list = []
    for e in ele:
        res_list.append(int(e))
    page_number_list.append(res_list)

#print(page_number_list)

update_index = 0
result = 0
while update_index < len(page_number_list):
    #print(check_update(ordering_rule_list, page_number_list[update_index]))
    current_update = page_number_list[update_index]
    if check_update(ordering_rule_list, current_update):
        result += current_update[int((len(current_update) - 1)/2)]
    update_index += 1

print(result)