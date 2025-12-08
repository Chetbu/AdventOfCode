import math
import time
from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

def dist(t1,t2):
    #distance between 2 tuples
    return math.sqrt((t1[0] - t2[0]) ** 2 + (t1[1] - t2[1]) ** 2 + (t1[2] - t2[2]) ** 2)


with open(file_filepath) as f:
    lines = f.read().splitlines()

#for you my Burg'
tuple_array = [(int(y[0]), int(y[1]), int(y[2])) for y in [x.split(',') for x in lines]]
# print(tuple_array)

distance_dict = {}
circuit_dict = {}
connection_available_array = []

for i, t1 in enumerate(tuple_array):
    j = 0
    circuit_dict[t1] = 0
    while j < i:
        t2 = tuple_array[j]
        distance_dict[(t1, t2)] = dist(t1,t2)
        connection_available_array.append((t1,t2))
        j += 1
# print(distance_dict.keys())

#sort by shortest distance
t_array = [(x,distance_dict[x]) for x in connection_available_array]
t_array.sort(key= lambda tup: tup[1])

i = 0
i_max = 100000
max_index_circuit = 1
everything_connected = False
while i < i_max and not everything_connected:
    #Find the shortest connexion available
    current_t = t_array.pop(0)
    connection_min = current_t[0]
    distance_min = current_t[1]

    #check if the connection is already linked to a circuit
    circuit_index = 0
    circuit_0 = circuit_dict[connection_min[0]]
    circuit_1 = circuit_dict[connection_min[1]]

    if circuit_0 == 0 and circuit_1 == 0:
        #create a new circuit
        circuit_index = max_index_circuit
        max_index_circuit += 1
    elif circuit_0 > 0 and circuit_1 > 0:
        #two circuit merging together
        circuit_index = circuit_0
        #change all the circuit_1 value to circuit 0
        for k in circuit_dict.keys():
            if circuit_dict[k] == circuit_1:
                circuit_dict[k] = circuit_0
    else:
        circuit_index = max(circuit_0, circuit_1)
    
    circuit_dict[connection_min[0]] = circuit_index
    circuit_dict[connection_min[1]] = circuit_index

    # print("Connexion found is ", connection_min, " seen in the circuit ", circuit_index)

    # print(set(circuit_dict.values()))
    if len(set(circuit_dict.values())) == 1:
        result = connection_min[0][0] * connection_min[1][0]
        print("everything connected for ", connection_min, " mult of X coord is ", result )
        everything_connected = True







 