# import math

# def arr_eval(arr):
#     return arr.split()

import time

rock_array = (
        (
            (1,1,1,1),
        ),
        (
            (0,1,0),
            (1,1,1),
            (0,1,0)
        ),
        ( #inverted because 0 in the tower is up
            (1,1,1),
            (0,0,1),
            (0,0,1)
        ),
        (
            (1,),
            (1,),
            (1,),
            (1,),
        ),
        (
            (1,1),
            (1,1)
        )

    )

def jet_dir(s:str, i:int):
    index = i % len(s)
    return s[index]

def expand_chamber(ch:list, i:int): #expend chamber to height i, return chamber if i < len chamber + 1 
    while len(ch) < i + 1:
        ch.append([1,0,0,0,0,0,0,0,1])
    return

def tower_h(ch:list): #return the height of the tower / highest element
    i = len(ch) - 1
    while not(1 in ch[i][1:8]):
        i = i - 1
    return i

def display_chamber(ch:list):
    i = 0
    while i < len(ch):
        print(ch[-1-i])
        i = i + 1
    return



def new_rock(ch:list, height:int, r_index:int, rock_arr:tuple):
    rock = rock_arr[r_index % len(rock_arr)]
    #print(rock)
    #add lines to the chamber to put the rock in
    expand_chamber(ch, height + len(rock))
    #starting position to print the rock is 3
    start_y = 3
    x = height

    coord_rock = [] #where is the rock
    while x - height < len(rock):
        y = start_y
        while y - start_y < len(rock[x - height]):
            if rock[x - height][y - start_y] == 1:
                ch[x][y] = 1 #draw chamber
                coord_rock.append([x,y])


            y = y + 1

        x = x + 1
    return (True, coord_rock)

def move_rock(ch:list, coor_rock_arr:list, direction:str):
    move_list = ("d","<",">")
    move_array = ((-1,0),(0,-1),(0,1))

    mov_i = move_list.index(direction)
    move = move_array[mov_i]
    coor_rock = coor_rock_arr[1]

    #calc the new coord
    n_coord_array = []
    for el in coor_rock:
        new_coord = [
            el[0] + move[0],
            el[1] + move[1]
        ]

        n_coord_array.append(new_coord)
    
    #test if can be moved, meaning all point in the chamber for the new coord are 0 if not the rock itself
    can_be_moved = True
    for el in n_coord_array:
        if not(el in coor_rock) and ch[el[0]][el[1]] == 1:
            can_be_moved = False
    
    if can_be_moved: #if can be moved, print the new rock in the chamber
        for el in coor_rock:
            ch[el[0]][el[1]] = 0
        for el in n_coord_array:
            ch[el[0]][el[1]] = 1
        return (True, n_coord_array)
    elif not(can_be_moved) and mov_i > 0: #regular move not possible
        return (True, coor_rock)
    else: #down not possible
        return (False, coor_rock)


        








 

with open('data.txt') as f:
    lines = f.read().splitlines()
    #lines_array = list(map(arr_eval,lines))

    jet_string = lines[0]
    #print(jet_dir(jet_string,3))

    ## line 2
    ## line 1 etc with 0 and 8 being rocks
    ## line 0 all rocks

    jet_i = 0
    rock_i = 0

    line_0 = [1]*9
    chamber = [line_0]

    st = time.time()

    h_array = []
    rec_array = []
    key_array = []

    test= [0,1,21,1,2,5]
    print(test[1:3])
    print(test[3:5] == test[1:3])

    #goal is that jet and rock array begins when creating a new rock / jet % len(jet) == 0 and same for rock

    m_move_down = 0
    stop_var = True

    target = 1000000000000        

    while rock_i < 10000 and stop_var:

        key = (rock_i % len(rock_array), jet_i % len(jet_string))
        key_array.append(key)
        h_array.append((rock_i, tower_h(chamber)))

        if key_array.count(key) >= 2:

            #look last 3 keys index
            i = len(key_array) - 1
            index_arr = []
            while len(index_arr)<3:
                if key_array[i] == key:
                    index_arr.insert(0,i)
                i = i - 1

            if key_array[index_arr[0]:index_arr[1]] == key_array[index_arr[1]:index_arr[2]]:
                stop_var = False
                h_beginning = h_array[index_arr[0]]
                h_recu = h_array[index_arr[1]]

                print(h_beginning)
                print(h_recu)

                x_recu = h_recu[0] - h_beginning[0]
                h_recu = h_recu[1] - h_beginning[1]


                angle = int((target-h_beginning[0])/x_recu)
                rest = (target-h_beginning[0]) % x_recu

                total_h = angle*h_recu + h_array[h_beginning[0] + rest][1]
                print(total_h)

          

        rock = new_rock(chamber,tower_h(chamber)+4,rock_i,rock_array)
        count_down = 0
        

        while rock[0]:
            rock = move_rock(chamber,rock,jet_dir(jet_string,jet_i))
            jet_i = jet_i + 1
            rock = move_rock(chamber,rock,"d")
            count_down = count_down + 1
        
        m_move_down = max(m_move_down, count_down)


        rock_i = rock_i + 1



    print("End ", time.time() - st)

    #print(tower_h(chamber))

 