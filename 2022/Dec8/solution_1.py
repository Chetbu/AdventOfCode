def arr_split(arr):
    return arr.split()

def is_hidden(x:int,y:int, arr):
    # horizontaltest
    height = arr[y][x]
    i = 0
    count_hidden = 0

    #print(arr[y][:x])
    #print(arr[y][x+1:])

    for letter in arr[y][:x]:
        if letter >= height:
            count_hidden = count_hidden + 1
            break

    for letter in arr[y][x+1:]:
        if letter >= height:
            count_hidden = count_hidden + 1
            break
    
    for word in arr[:y]:
        if word[x] >= height:
            count_hidden = count_hidden + 1
            break

    for word in arr[y+1:]:
        if word[x] >= height:
            count_hidden = count_hidden + 1
            break
    
    return count_hidden

def scenic_score(x:int,y:int, arr):
    h_boundary = len(arr[0])
    v_boundary = len(arr)

    scenic_score = 1
    height = arr[y][x]
    i = 1
    while arr[y][x-i] < height:
        if (x-i) == 0:
            break
        i = i + 1
    #print(i)
    scenic_score = scenic_score * i

    i = 1
    while arr[y][x+i] < height:
        if (x + i) == h_boundary - 1:
            break
        i = i + 1
    #print(i)
    scenic_score = scenic_score * i

    i = 1
    while arr[y-i][x] < height:
        
        if (y-i) == 0:
            break
        i = i + 1
    #print(i)
    scenic_score = scenic_score * i

    i = 1
    while arr[y+i][x] < height:
        
        if (y + i) == v_boundary - 1:
            break
        i = i + 1
    #print(i)
    scenic_score = scenic_score * i

    return scenic_score




with open('data.txt') as f:
    lines = f.read().splitlines()
    ##lines_array = list(map(arr_split,lines))

    h_boundary = len(lines[0])
    v_boundary = len(lines)


    x = 1

    ##print(scenic_score(2,3,lines))

    # count_visible = 2*((h_boundary - 1) + (v_boundary - 1))

    # while x < h_boundary - 1:
    #     z = 1
    #     while z < v_boundary - 1:
    #         ##print([x,z])
    #         if is_hidden(x,z,lines) < 4:
    #             count_visible = count_visible + 1
    #         z = z + 1
    #     x = x + 1

    ##print(count_visible)
    max_score = 0

    while x < h_boundary - 1:
        z = 1
        while z < v_boundary - 1:
            score = scenic_score(x,z,lines)
            if score > max_score:
                max_score = score
            z = z + 1
        x = x + 1

    print(max_score)






    
    












