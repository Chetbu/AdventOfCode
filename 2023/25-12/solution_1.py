# import math
import copy
# import time



def eval_linked_nodes(node, memory_dict, l_dict):
    p_next_node_arr = l_dict[node]
    trace_arr = memory_dict[node] + [node]

    #print("trace_arr", trace_arr)

    new_node_to_explore = []

    for n in p_next_node_arr:
        old_memory = memory_dict[n]
        if len(trace_arr) < len(old_memory) or old_memory ==[]:
            # add it to the memory
            memory_dict[n] = trace_arr
            # Add this node the the list of node to reconsider
            new_node_to_explore.append(n)
    return (memory_dict, new_node_to_explore)
            

def find_shortest_route(start_node, exit_node, l_dict):
    memory_dict = dict.fromkeys(l_dict)
    for key in memory_dict:
        memory_dict[key] = []
    #print(memory_dict)
    
    shortest_route = []

    node_to_eval_arr = [start_node]
    while len(node_to_eval_arr) > 0:
        node_to_probe = node_to_eval_arr.pop(0)
        res_eval = eval_linked_nodes(node_to_probe, memory_dict, l_dict)
        memory_dict = res_eval[0]
        new_node_arr = res_eval[1]

        if exit_node in new_node_arr:
            new_route = memory_dict[exit_node]
            if len(new_route) < len(shortest_route) or shortest_route == []:
                #new shortest route defined
                shortest_route = new_route
            new_node_arr.remove(exit_node)
        node_to_eval_arr = node_to_eval_arr + new_node_arr

        
    if shortest_route != []:
        return (True, shortest_route + [exit_node])
    else:
        return (False, [])

def calc_new_link_d(l_dict, route):
    #goal here is to erase for existing dict all the links used by the route
    i = 1
    new_l_dict = copy.deepcopy(l_dict)
    while i < len(route):
        node_1 = route[i-1]
        node_2 = route[i]

        r1 = new_l_dict[node_1]
        r1.remove(node_2)
        new_l_dict[node_1] = r1

        r2 = new_l_dict[node_2]
        r2.remove(node_1)
        new_l_dict[node_2] = r2
        i += 1
    
    return new_l_dict

def calc_number_of_links(start_node, exit_node, l_dict):
    current_l_dict = copy.deepcopy(l_dict)
    route_arr = []
    current_route_calc = find_shortest_route(start_node, exit_node, current_l_dict)
    count = 0
    while current_route_calc[0] and count < 4:
        route_arr.append(current_route_calc[1])
        current_l_dict = calc_new_link_d(current_l_dict,current_route_calc[1])
        current_route_calc = find_shortest_route(start_node, exit_node, current_l_dict)
        count += 1
    return count




with open('data.txt') as f:
    lines = f.read().splitlines()

#print(lines)

link_dict = dict()

for line in lines:
    temp1 = line.split(":")
    origin_node = temp1[0]
    target_arr = temp1[1].split(" ")[1:]

    if not origin_node in link_dict:
        link_dict[origin_node] = target_arr
    else:
        link_dict[origin_node] = link_dict[origin_node] + target_arr
    
    for t_node in target_arr:
        if not t_node in link_dict:
            link_dict[t_node] = [origin_node]
        else:
            link_dict[t_node] = link_dict[t_node] + [origin_node]

#print(len(link_dict))


#test_shortest_route = find_shortest_route("jqt", "cmg", link_dict)
#print(test_shortest_route)

# print(calc_new_link_d(link_dict, test_shortest_route))
# print((link_dict))
            
#print(calc_number_of_links("jqt", "cmg", link_dict))
#print(calc_number_of_links("jqt", "ntq", link_dict))
            
# t_n1 = list(link_dict)[0]

# t_n2 = list(link_dict)[-1]
# print(calc_number_of_links(t_n1, t_n2, link_dict))

l_nodes = list(link_dict)
start_node = l_nodes[0]

i = 1
start_node_group = [start_node]
opposite_group = []
while i < len(l_nodes):
    end_n = l_nodes[i]
    calc_v = calc_number_of_links(start_node, end_n,link_dict)
    if calc_v > 3:
        start_node_group.append(end_n)
    else:
        opposite_group.append(end_n)

    i += 1

#print(start_node_group)
#print(opposite_group)
print(len(start_node_group) * len(opposite_group))