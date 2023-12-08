def coord(a:str):
    if a == "A" or a == "X":
        return 0
    elif a == "B" or a == "Y":
        return 1
    elif a == "C" or a == "Z":
        return 2
    return -1

def point(a:str):
    res = list(map(coord, a.split()))

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
