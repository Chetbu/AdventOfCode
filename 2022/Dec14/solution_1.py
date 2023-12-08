
def arr_eval(arr):
    return arr.split(" -> ")

def is_bloqued(x:int,y:int, rock_array, sand_array):
    res = False
    if [x,y] in rock_array:
        res = True
    elif [x,y] in sand_array:
        res = True
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
    for rock in rock_coord:
        last_rock_y = max(last_rock_y, rock[1])

    #print(rock_coord)
    #print(is_bloqued(49,9,rock_coord,[[49,9]]))
    print(last_rock_y)

    i = 1
    init = [500,0]
    count = 0
    fall = True
    sand_coord = [[500,8]]
    while fall:
        c_sand = init
        move = True
        co = 0
        #print("sand_coord is",sand_coord)
        while move and co < last_rock_y + 1:
            #print(c_sand)
            co = co + 1
            if is_bloqued(c_sand[0],c_sand[1] + 1,rock_coord,sand_coord) == False:
                c_sand = [c_sand[0], c_sand[1] + 1]
            elif is_bloqued(c_sand[0]-1,c_sand[1] + 1,rock_coord,sand_coord) == False:
                c_sand = [c_sand[0]-1, c_sand[1] + 1]
                #print("left")
            elif is_bloqued(c_sand[0]+1,c_sand[1] + 1,rock_coord,sand_coord) == False:
                c_sand = [c_sand[0]+1, c_sand[1] + 1]
                #print("right")
            else:
                move = False
                sand_coord.append([c_sand[0],c_sand[1]])
        if co ==  last_rock_y + 1:
            fall = False  
        count = count + 1
    print(count)
        











   