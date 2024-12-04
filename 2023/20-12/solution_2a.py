# import math
# import copy
import time
import math

def return_relay(relay_str, relay_arr):
    temp_arr = [x[0] for x in relay_arr]
    #print(relay_str, relay_arr)
    i_relay = temp_arr.index(relay_str)
    return relay_arr[i_relay]

def change_state(relay_str, relay_arr, state_array, conj_prede_arr, input):
    relay = return_relay(relay_str, relay_arr)
    if relay[1] == "%":
        if input == "high":
            #ignored, no chage of state, return existing
            return 0
        elif input == "low":
            #chage state and return the new state
            current_state = state_array[relay_str]
            if current_state == "low":
                target_state = "high"
            else:
                target_state = "low"
            state_array[relay_str] = target_state
            return target_state
    elif relay[1] == "&":
        prede_arr = conj_prede_arr[relay_str]
        target_state = "low"
        for p_arr in prede_arr:
            if relay_state[p_arr] == "low":
                target_state = "high"
        state_array[relay_str] = target_state
        return target_state
    else:
        print("error")

        return 0
       



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

#need to track the predecessors for & relays
conj_array = [x[0] for x in relay_arr if x[1] == "&"]

conj_predecessor_dict = dict.fromkeys(conj_array)


for c_relay_name in conj_array:
    for relay in relay_arr:
        if c_relay_name in relay[2]:

            if conj_predecessor_dict[c_relay_name] == None:
                conj_predecessor_dict[c_relay_name] = [relay[0]]
            else:
                conj_predecessor_dict[c_relay_name] = conj_predecessor_dict[c_relay_name] + [relay[0]]


#now let's push the button and run the signal
i = 0
i_limit = 5000


start_end_arr = [
    ("zs", "vg"),
    ("cg", "gs"),
    ("dt", "kd"),
    ("sr", "zf")
]

end_t = ("vg", "gs", "kd", "zf")
loop_nodes = [
    ['zs', 'kx', 'bj', 'zs', 'br', 'jd', 'bj', 'vg'], 
    ['cg', 'qx', 'rj', 'gs', 'sb', 'qx', 'qf', 'gz', 'hl', 'cg'], 
    ['dt', 'tg', 'tq', 'tp', 'rb', 'dt', 'kd', 'zt'], 
    ['sr', 'pf', 'zd', 'tr', 'hr', 'zf', 'sr', 'xq', 'pm', 'lc']
    ]

end_i = 0
end_relay = end_t[end_i] 
start_time = time.time()
split_time = time.time()

while i < i_limit:
    s_arr = list(signal_init_t)
    j = 0
    while j < len(s_arr):
        destination_relay = s_arr[j][0]

        if destination_relay in [x[0] for x in relay_arr]:

            signal_intensity = s_arr[j][1]
            output = change_state(destination_relay, relay_arr, relay_state,conj_predecessor_dict,signal_intensity)
            #print(relay_arr)

            if output != 0:

                full_relay = return_relay(destination_relay, relay_arr)
                for next_relay in full_relay[2]:
                    next_signal = (next_relay, output)
                    if next_signal == ("rg", "high"):
                        print(i+1)
                    s_arr.append((next_relay, output))

        


        j += 1


        #print(r, relay_state[r])
    
    if i % 100 == 0:
        print(i, time.time() - split_time)
        split_time = time.time()
        #print(s_arr)

    
    i+=1

print(math.lcm(3767,3779,4057,3889))