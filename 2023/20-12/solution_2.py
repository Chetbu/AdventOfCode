# import math
# import copy
import time


def return_relay(relay_str, relay_arr):
    temp_arr = [x[0] for x in list(relay_arr)]
    #print(relay_str, relay_arr)
    i_relay = temp_arr.index(relay_str)
    return relay_arr[i_relay]


def return_relay_state_index(relay_str, relay_state_t):
    temp_arr = [x[0] for x in list(relay_state_t)]
    #print(relay_str, relay_arr)
    return temp_arr.index(relay_str)


def change_state_tuple(relay_state_t, i_tuple, target_state, relay_str):
    return relay_state_t[:i_tuple] + ((relay_str, target_state),) + relay_state_t[i_tuple+1:]

# test_tuple_state = (('a', 'low'), ('b', 'low'), ('c', 'low'), ('inv', 'low'))
# print("test", change_state_tuple(test_tuple_state, 3, "high", "b"))


def change_state(relay_str, relay_arr, relay_state_t, conj_prede_arr, input):
    relay = return_relay(relay_str, relay_arr)
    i_relay_state = return_relay_state_index(relay_str, relay_state_t)
    if relay[1] == "%":
        if input == "high":
            #ignored, no chage of state, return existing
            return (0, relay_state_t)
        elif input == "low":
            #chage state and return the new state
            current_state = relay_state_t[i_relay_state][1]
            if current_state == "low":
                target_state = "high"
            else:
                target_state = "low"
            relay_state_t = change_state_tuple(relay_state_t,i_relay_state,target_state,relay_str)
            return (target_state, relay_state_t)
    elif relay[1] == "&":
        temp_l = [x[0] for x in list(conj_prede_arr)]
        i_conjug = temp_l.index(relay_str)
        prede_arr = conj_prede_arr[i_conjug][1]
        target_state = "low"
        for p_arr in prede_arr:
            if relay_state[p_arr] == "low":
                target_state = "high"
        relay_state_t = change_state_tuple(relay_state_t,i_relay_state,target_state,relay_str)
        return (target_state, relay_state_t)
    else:
        print("error")
        return 0
       

def propagate(start_relay_str, relay_arr, relay_state_t,conj_predecessor_t, end_str):
    s_arr = [(start_relay_str, "low")]
    j = 0
    while j < len(s_arr):
        destination_relay = s_arr[j][0]

        if destination_relay in [x[0] for x in relay_arr] and destination_relay != end_str:

            signal_intensity = s_arr[j][1]
            output = change_state(destination_relay, relay_arr, relay_state_t,conj_predecessor_t,signal_intensity)
            #print(relay_arr)

            if output[0] != 0:
                relay_state_t = output[1]

                full_relay = return_relay(destination_relay, relay_arr)
                for next_relay in full_relay[2]:
                    next_signal = (next_relay, output[0])

                    s_arr.append(next_signal)

    


        j += 1 
    return (s_arr, relay_state_t)


with open('data.txt') as f:
    lines = f.read().splitlines()

#print(lines)

relay_arr = []
relay_state = dict()

signal_arr = []

for line in lines:
    temp = line.split(" -> ")
    if temp[0] == "broadcaster":
        relay_arr.append((temp[0], "init", tuple(temp[1].split(", "))))
        for r_str in temp[1].split(", "):
            signal_arr.append((r_str, "low"))
    else:
        relay_arr.append((temp[0][1:], temp[0][0], tuple(temp[1].split(", "))))
        if temp[0][0] == "%":
            relay_state[temp[0][1:]] = "low"
        else:
            relay_state[temp[0][1:]] = "low"

signal_init_t = tuple(signal_arr)
#print(signal_init_t)
signal_init_t = (("zs","low"),)

relay_arr_t = tuple(relay_arr)
#print(signal_init_t)

relay_state_t = tuple(list(relay_state.items()))
#print(relay_state_t)

relay_state_t_history = [relay_state_t]

#need to track the predecessors for & relays
conj_array = [x[0] for x in relay_arr if x[1] == "&"]

conj_predecessor_dict = dict.fromkeys(conj_array)


for c_relay_name in conj_array:
    for relay in relay_arr:
        if c_relay_name in relay[2]:

            if conj_predecessor_dict[c_relay_name] == None:
                conj_predecessor_dict[c_relay_name] = tuple([relay[0]])
            else:
                conj_predecessor_dict[c_relay_name] = tuple(list(conj_predecessor_dict[c_relay_name]) + [relay[0]])


conj_predecessor_t = tuple(list(conj_predecessor_dict.items()))


# loop test

start_end_arr = [
    ("zs", "vg"),
    ("cg", "gs"),
    ("dt", "kd"),
    ("sr", "zf")
]

loop_nodes = []
for s_e in start_end_arr:
    s_arr = propagate(s_e[0], relay_arr_t, relay_state_t, conj_predecessor_t, s_e[1])[0]
    #print(s_arr)
    temp = [x[0] for x in s_arr]
    loop_nodes.append(temp)

print(loop_nodes)
#print(conj_predecessor_t)

#now let's push the button and run the signal
i = 0
i_limit = 10000000
split_time = time.time()

rx_low_found = False

start_time = time.time()
# reinit 
relay_state_t = tuple(list(relay_state.items()))
i_s_e = 0
while i < i_limit and not rx_low_found:
    s_e = start_end_arr[i_s_e]
    prop = propagate(s_e[0], relay_arr_t, relay_state_t, conj_predecessor_t, s_e[1])
    relay_state_t = prop[1]
    s_arr = prop[0]

    i_end = [x[0] for x in s_arr].index(s_e[1])
    state_end = s_arr[i_end][1]
    if state_end == "low":
        print(s_arr[i_end], i)

    
    i+=1

    #print(s_arr)
