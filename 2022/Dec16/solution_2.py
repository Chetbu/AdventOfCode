import math
import time

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

def create_partition_array(arr, l:int):
    if l > 0:
        res = []
        for el in arr:
            res.append(el + (True,))
            res.append(el + (False,))
        return create_partition_array(res, l - 1)
    else:
        return [(True,), (False,)]


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


 

with open('data.txt') as f:

    st = time.time()
    
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
    print((w_valve_arr[:3]))
    print((w_valve_arr[3:]))
   

    # test_arr = [True] * len(w_valve_arr)
    # test_arr[1] = False

    print("Data is ready ", time.time() - st)
    st = time.time()



    print(len(w_valve_arr))



    permutation = [(True,), (False,)]
    i = 14
    while i > 0:
        temp_permut = []
        for el in permutation:
            temp_permut.append(el + (True,))
            temp_permut.append(el + (False,))
        permutation = temp_permut
        i = i - 1
    
    temp_permut = []
    for el in permutation:
        temp_permut.append((True,) + el)
    permutation = temp_permut

    print("permutation time ", time.time() - st)
    # print((permutation[-2]))
    # print((permutation[1]))

    # i = 0
    # array = []
    # while i < len(permutation):
    #     j = 0
    #     while j < len(permutation[i]):
    #         if permutation[i][j] == permutation[-i-1][j]:
    #             array.append(i)
    #         j = j + 1
    #     i = i + 1
    # print(len(array))
    st = time.time()

    total_i = len(permutation)
    print(total_i)

    i = 0
    max_pression = 0
    while i < len(permutation):
        calc_human = calc_move('AA', 27, 0, w_valve_arr, w_dist_arr, permutation[i])
        calc_elephant = calc_move('AA', 27, 0, w_valve_arr, w_dist_arr, permutation[-i-1])

        max_pression = max(max_pression, (calc_elephant + calc_human))


        i = i + 1
        if i % 100 == 0:
            print(100*i/total_i)

    print(max_pression)


    

    #print(calc_move('AA', 31, 0, w_valve_arr, w_dist_arr, tuple(w_v_status_arr)))

    print("End ", time.time() - st)
    




    #print(calc_move(w_valve_arr[0][0], 80, 0, w_valve_arr, w_dist_arr, tuple(test_arr)))

    







    






        


   