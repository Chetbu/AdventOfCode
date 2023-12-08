def coord(a:str):
    if a == "A":
        return 0
    elif a == "B":
        return 1
    elif a == "C":
        return 2
    elif a == "X":
        return -1
    elif a == "Y":
        return 0
    elif a == "Z":
        return 1
    return -10
    

def point(a:str):
    res1 = list(map(coord, a.split()))

    y_coord = res1[0] + res1[1]
    if y_coord == -1:
        y_coord = 2
    elif y_coord == 3:
        y_coord = 0

    res = [res1[0],y_coord]



    ##print(res)

    win_matrix = [
        [3,6,0],
        [0,3,6],
        [6,0,3]
    ]
    ## 0 if loss, 3 draw, 6 win

    result = win_matrix[res[0]][res[1]]

    ## score = win score + 1, 2 or 3 if rock paper scissors
    return result + 1 + res[1]



with open('data.txt') as f:
    lines = f.read().splitlines()

    total_score = 0

    for line in lines:
        total_score = total_score + point(line)

        ##print(point(line))

    print(total_score)
