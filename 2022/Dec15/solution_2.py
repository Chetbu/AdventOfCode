
def arr_eval(arr):
    return arr.split()

def removeDuplicates(lst):     
    return list(set([i for i in lst]))

def dist(coor_beacon, coor_sensor):
    dist_x = abs(coor_beacon[0] - coor_sensor[0])
    dist_y = abs(coor_beacon[1] - coor_sensor[1])
    return int(dist_x + dist_y)

  

with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_eval,lines))

    data = []
    for line in lines_array:
        coord_sensor = (int(line[2][2:-1]),int(line[3][2:-1]))
        coord_beacon = (int(line[8][2:-1]),int(line[9][2:]))

        data.append((coord_sensor, coord_beacon, dist(coord_sensor, coord_beacon)))
    
    print("data is ready")

    min_c = 0
    max_c = 1+4000000
    y = min_c
    stop_var = True
    arr = []
 
    for line in data:
        sensor = line[0]
        distance= line[2] + 1
        step = distance
        while step >= 0:
            if 0 <= sensor[0] + distance - step < max_c:
                if 0 <= sensor[1] + step < max_c:
                    arr.append((sensor[0] + distance - step, sensor[1] + step))
                if 0 <= sensor[1] - step < max_c:
                    arr.append((sensor[0] + distance - step, sensor[1] - step))
            if 0 <= sensor[0] - (distance - step) < max_c:
                if 0 <= sensor[1] + step < max_c:
                    arr.append((sensor[0] - (distance - step), sensor[1] + step))
                if 0 <= sensor[1] - step < max_c:
                    arr.append((sensor[0] - (distance - step), sensor[1] - step))           
            step = step - 1

        print("line")
    #print(arr)

    print("len beginning ", len(arr))

    # i = len(arr) - 1

    # while i >= 0:
    #     if min_c > arr[i][0] or min_c > arr[i][1] or max_c < arr[i][0] or max_c < arr[i][1]:
    #         #print("del ", arr[i])
    #         #print(arr[i][1])
    #         del arr[i]


    #     i = i - 1
    #     if i % 1000000 == 0:
    #         print("i outbound, ",i)
    
    print("len after limit outbound ",len(arr))

    res = removeDuplicates(arr)

    print("len after dedup ", len(res))
    #print(res)

    i = 0
    stop_var = True
    while i < len(res) and stop_var:
        j = 0
        undetected = True
        #print(res[i])
        while j < len(data) and undetected:
            if dist(data[j][0], res[i]) <= data[j][2]:
                undetected = False

            j = j + 1
        if undetected:
            stop_var = False
            print("Result ",res[i])
            print("Tuning ", 4000000 * res[i][0] + res[i][1])
        i = i + 1
        if i % 1000000 == 0:
            print("i outbound, ",i)




 


   