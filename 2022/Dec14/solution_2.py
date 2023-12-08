
def arr_eval(arr):
    return arr.split(" -> ")

def is_bloqued(x:int,y:int, rock_array):
    res = False
    if [x,y] in rock_array:
        res = True
    return res

def clean_array(x:int,y:int, rock_array):
    res = []
    for rock in rock_array:
        if rock[0] != x:
            res.append(rock)
        elif rock[1] < y+2:
            res.append(rock)
    return res


 

with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_eval,lines))

    rock_coord = []
    for line in lines_array:
        coord_array = []
        for rock in line:
            coord = list(rock.split(","))
            coord_array.append([int(coord[0]),int(coord[1])])
        i = 1
        rock_coord.append([coord_array[0][0],coord_array[0][1]])

        while i < len(coord_array):
            if coord_array[i-1][0] == coord_array[i][0]:
                step = [0, int(abs(coord_array[i-1][1] - coord_array[i][1])/(coord_array[i][1] - coord_array[i-1][1]))]

                    
            elif coord_array[i-1][1] == coord_array[i][1]:
                step = [int(abs(coord_array[i-1][0] - coord_array[i][0])/(coord_array[i][0] - coord_array[i-1][0])), 0]

            else:
                print("error")
            c_coord = coord_array[i-1]
            #print(c_coord)
            while c_coord != coord_array[i]:
                c_coord[0] = c_coord[0] + step[0]
                c_coord[1] = c_coord[1] + step[1]
                #print(c_coord)
                rock_coord.append([c_coord[0],c_coord[1]])
            

            i = i + 1

    last_rock_y = 0
    min_rock_x = 500
    max_rock_x = 500
    for rock in rock_coord:
        last_rock_y = max(last_rock_y, rock[1])

    x = 500 - last_rock_y - 5
    while x < 500 + last_rock_y + 5:
        rock_coord.append([x,last_rock_y + 2])
        x = x + 1
        

    #print(rock_coord)
    #print(clean_array(498, 6, rock_coord))
    #print(is_bloqued(49,9,rock_coord,[[49,9]]))
    #print(last_rock_y, min_rock_x, max_rock_x)

    i = 1
    init = [500,0]
    count = 0
    fall = True

    while fall:
        c_sand = init
        move = True
        co = 0
        #print("sand_coord is",sand_coord)
        while move:
            #print(c_sand)
            
            if is_bloqued(c_sand[0],c_sand[1] + 1,rock_coord) == False:
                c_sand = [c_sand[0], c_sand[1] + 1]
                co = co + 1
            elif is_bloqued(c_sand[0]-1,c_sand[1] + 1,rock_coord) == False:
                c_sand = [c_sand[0]-1, c_sand[1] + 1]
                co = co + 1
                #print("left")
            elif is_bloqued(c_sand[0]+1,c_sand[1] + 1,rock_coord) == False:
                c_sand = [c_sand[0]+1, c_sand[1] + 1]
                co = co + 1
                #print("right")
            else:
                move = False
                #rock_coord = [x for x in rock_coord if x[0] != c_sand[0]]
                #sand_coord = [x for x in sand_coord if x[0] != c_sand[0]]
                try:
                    rock_coord.remove([c_sand[0],c_sand[1]+2])
                except ValueError:
                    pass

                #rock_coord = clean_array(c_sand[0],c_sand[1],rock_coord)

                rock_coord.append([c_sand[0],c_sand[1]])
                if count % 50 == 0:
                    print([c_sand[0],c_sand[1]])

                i = 0
                
            if co == 0:
                fall = False

        count = count + 1
    print(count)
        











   