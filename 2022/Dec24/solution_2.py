# import math
# import copy
import time
import pickle

moves = (
    (0,0),
    (-1,0),
    (1,0),
    (0,-1),
    (0,1)
)

st = time.time()

def is_empty(state:tuple):

    return state[1] in time_space_t[state[0] % len(time_space_t)]

def extract_coor(b:tuple):
    return b[1]

def possible_moves(state:tuple):
    res = []
    round = state[0] + 1
    for move in moves:
        new_coor = (
            state[1][0] + move[0],
            state[1][1] + move[1]
        )

        if is_empty((round, new_coor)):
            res.append((round, new_coor))
    return res




with open('data_output.pickle', 'rb') as f:
     time_space_t = pickle.load(f)

#first go to exit

init = (0, (0,1))
end_coor = time_space_t[0][1]
move_arr = [init]
st = time.time()

current_round = 0
stop_variable = True
while len(move_arr) > 0 and stop_variable:
    if move_arr[0][0] > current_round:
        current_round = move_arr[0][0]
        move_arr = list(set(move_arr))
        list_coor = list(map(extract_coor, move_arr))
        if end_coor in list_coor:
            stop_variable = False
            print("route is solved in :", current_round, "elapsed time :", time.time() - st)
    else:
        state = move_arr.pop(0)
        for el in possible_moves(state):
            move_arr.append(el)

#back to the start

init = (current_round, end_coor)
end2_coor = (0,1)
move_arr = [init]
st = time.time()


stop_variable = True
while len(move_arr) > 0 and stop_variable:
    if move_arr[0][0] > current_round:
        current_round = move_arr[0][0]
        move_arr = list(set(move_arr))
        list_coor = list(map(extract_coor, move_arr))
        if end2_coor in list_coor:
            stop_variable = False
            print("back route is solved in :", current_round, "elapsed time :", time.time() - st)
    else:
        state = move_arr.pop(0)
        for el in possible_moves(state):
            move_arr.append(el)

#back to the end
st = time.time()
init = (current_round, (0,1))
end_coor = time_space_t[0][1]
move_arr = [init]


stop_variable = True
while len(move_arr) > 0 and stop_variable:
    if move_arr[0][0] > current_round:
        current_round = move_arr[0][0]
        move_arr = list(set(move_arr))
        list_coor = list(map(extract_coor, move_arr))
        if end_coor in list_coor:
            stop_variable = False
            print("2nd route is solved in :", current_round, "elapsed time :", time.time() - st)
    else:
        state = move_arr.pop(0)
        for el in possible_moves(state):
            move_arr.append(el)











    






 