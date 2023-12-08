def arr_split(arr):
    return arr.split()

def head_move(s:str, pos:list):
    x = pos[0]
    y = pos[1]

    move_array = [
        ["R",[0,1]],
        ["L",[0,-1]],
        ["U",[1,0]],
        ["D",[-1,0]]
    ]

    for move in move_array:
        if move[0] == s:
            x = move[1][0] + x
            y = move[1][1] + y

    return [x,y]

def tail_move_old(head_pos:list, old_head_pos: list, pos:list):
    x = pos[0]
    y = pos[1]

    head_x = head_pos[0]
    head_y = head_pos[1]

    if abs(x - head_x) <= 1 and abs(y - head_y) <= 1:
        return pos
    else:
        return old_head_pos

def tail_move(head_pos:list, pos:list):
    x = pos[0]
    y = pos[1]

    head_x = head_pos[0]
    head_y = head_pos[1]

    if abs(x - head_x) <= 1 and abs(y - head_y) <= 1:
        return pos
    elif x - head_x == 0:
        y = y - (y - head_y)/abs(y - head_y)
        return [int(x),int(y)]
    elif y - head_y == 0:
        x = x - (x - head_x)/abs(x - head_x)
        return [int(x),int(y)]
    else:
        x = x - (x - head_x)/abs(x - head_x)
        y = y - (y - head_y)/abs(y - head_y)
        return [int(x),int(y)] 


with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_split,lines))

    head_pos = [0,0]
    tail_pos = [0,0]

    all_tail_pos = []
    all_tail_pos_old = []

    for line in lines_array:
        direction = line[0]
        i = int(line[1])
        while i>0:
            old_head_pos = head_pos

            head_pos = head_move(direction, head_pos)
            #print(head_pos)
            tail_pos_old = tail_move_old(head_pos, old_head_pos, tail_pos)
            tail_pos = tail_move(head_pos, tail_pos)
            if (tail_pos != tail_pos_old):
                print(line)

            #print(tail_pos)
            #print(tail_pos_old)
            all_tail_pos.append(str(tail_pos[0])+"i"+str(tail_pos[1]))
            all_tail_pos_old.append(str(tail_pos_old[0])+"i"+str(tail_pos_old[1]))
            i = i - 1

    #print(all_tail_pos)
    
    #print(len(list(set(all_tail_pos))))
    #print(len(list(set(all_tail_pos_old))))

    rope = [[0,0]] * 10
    all_tail_pos = []


    for line in lines_array:
        direction = line[0]
        i = int(line[1])
        while i>0:
            rope[0] = head_move(direction, rope[0])
            k = 1
            while k < len(rope):
                rope[k] = tail_move(rope[k-1], rope[k])
                k = k + 1

            all_tail_pos.append(str(rope[9][0])+"i"+str(rope[9][1]))
            i = i - 1


    
    print(rope)
    print(len(list(set(all_tail_pos))))






   

    
    












