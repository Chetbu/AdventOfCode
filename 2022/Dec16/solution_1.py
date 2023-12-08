import math

def arr_eval(arr):
    return arr.split()

def search_valve(s:str, arr:list):
    i = 0
    while i < len(arr):
        if arr[i][0] == s:
            return arr[i]
        i = i + 1
    raise ValueError("No valve found with name ", s)

def distance(valve : str, valve_dest : str, already_visited_valves: tuple, data:list):
    v1_array = search_valve(valve, data)
    #print(v1_array)
    if valve_dest in v1_array[2]:
        return 1
    else:
        res = []
        for tunnel in v1_array[2]:
            if not(tunnel in already_visited_valves):
                visited = already_visited_valves + (valve, )
                res.append(distance(tunnel, valve_dest, visited, data) + 1)
            else:
                res.append(math.inf)
                #print(valve, res, already_visited_valves)
        return min(res)

def calc_move(current_valve : str, moves_left : int, pressure : int, w_valve_array:list, w_dist_array:list, w_v_status_array:tuple):
    #print(current_valve, moves_left)
    if moves_left <= 0: ## if no moves left, return old pressure
        
        return pressure
    else:
        c_v_index = -1 #find index of the current valve 
        i = 0
        while i < len(w_valve_array):
            if w_valve_array[i][0] == current_valve:
                c_v_index = i
            i = i + 1

        status_arr = list(w_v_status_array)
        status_arr[c_v_index] = True #open the valve
        st_tupple = tuple(status_arr)
        additional_pressure = w_valve_array[c_v_index][1] * (moves_left - 1) #calculate the additional pressure relieve by the action
        #print("additional P ",additional_pressure)


        v_index = 0
        res = [pressure + additional_pressure]
        while v_index < len(w_valve_array):
            if not(st_tupple[v_index]): #if the valve is not open
                d = w_dist_array[c_v_index][v_index] # #of moves to get to the new node

                res.append(calc_move(w_valve_array[v_index][0], moves_left - d - 1, pressure + additional_pressure, w_valve_array, w_dist_array, st_tupple))

            v_index = v_index + 1
        #print(current_valve, res)
        return max(res)


 

with open('test.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_eval,lines))

    #print(lines_array)
    data = []
    for line in lines_array:
        name = line[1]
        rate = int(line[4][5:-1])
        i = 9
        liste = []
        while i < len(line):
            if i == len(line) - 1:
                liste.append(line[i])
            else:
                liste.append(line[i][:-1])
            i = i + 1
        data.append([name, rate, tuple(liste)])
    #print(data[9][2][0])

    #print(data)

    #goal is to compute minimal travel distance between all the working valves, meaning nodes with a positive rate

    w_valve_arr = [['AA', 0]] #array of working valve + their rate
    for valve_arr in data:
        if valve_arr[1] > 0:
            w_valve_arr.append([valve_arr[0],valve_arr[1]])

    #print(w_valve_arr)

    #print(distance("HH","JJ",(),data))

    w_dist_arr = [] #is the arr with only nodes with a positive rate / and distance in between them

    i=0
    while i < len(w_valve_arr): #init
        w_dist_arr.append([0]*len(w_valve_arr))
        i = i + 1

    i = 0

    while i < len(w_valve_arr) - 1:
        j = i + 1
        while j < len(w_valve_arr):
            dist = distance(w_valve_arr[i][0],w_valve_arr[j][0],(),data)
            w_dist_arr[i][j] = dist
            w_dist_arr[j][i] = dist
            j = j + 1
        i = i + 1

    #print(w_dist_arr)

    w_v_status_arr = [False] * len(w_valve_arr) #is the valve open or not

    #print(w_v_status_arr)

    # test_arr = [True] * len(w_valve_arr)
    # test_arr[1] = False

    print(w_valve_arr)

    print(calc_move('AA', 3, 0, w_valve_arr, w_dist_arr, tuple(w_v_status_arr)))
    #print(calc_move(w_valve_arr[0][0], 80, 0, w_valve_arr, w_dist_arr, tuple(test_arr)))

    







    






        


   