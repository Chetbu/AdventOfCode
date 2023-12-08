
def arr_eval(arr):
    return arr.split()

def dist(coor_beacon, coor_sensor):
    dist_x = abs(coor_beacon[0] - coor_sensor[0])
    dist_y = abs(coor_beacon[1] - coor_sensor[1])
    return int(dist_x + dist_y)

  

with open('test.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_eval,lines))

    data = []
    max_x = 0
    min_x = 1384790

    for line in lines_array:
        coord_sensor = [int(line[2][2:-1]),int(line[3][2:-1])]
        coord_beacon = [int(line[8][2:-1]),int(line[9][2:])]
        max_x = max(max_x, coord_sensor[0] + dist(coord_sensor, coord_beacon))
        min_x = min(min_x, coord_sensor[0] - dist(coord_sensor, coord_beacon))
        data.append([coord_sensor, coord_beacon, dist(coord_sensor, coord_beacon)])
    

    y = 2000000
    print(min_x, max_x)
    x = min_x - 1
    res = []
    while x <= max_x + 1:
        detected = False
        for line in data:
            if dist([x,y],line[0]) <= line[2]:
                detected = True
                res.append([x,y])
                break
            
        x = x + 1

    for line in data:
        try:
            res.remove(line[1])
        except ValueError:
            pass
    #print(res)
    print(len(res))


   