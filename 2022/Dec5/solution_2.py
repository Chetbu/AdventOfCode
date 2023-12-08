def move_crates(arr, iteration:int, start:int, end:int):
    new_arr = arr
    crate_array = arr[start][len(arr[start])-iteration:]
    
    new_arr[start] = arr[start][:len(arr[start])-iteration]
    for crate in crate_array:
        new_arr[end].append(crate)
    return new_arr





with open('data_2.txt') as f:
    lines = f.read().splitlines()

    stack_array = []
    l = 0
    while l< len(lines)-1:
        stack_array.append([])

        l = l + 1
    
    l = 0

    while l< len(lines)-1:
        i = 0
        while i < len(lines[l]):
            stack_array[l].append(lines[l][i:i+3])
            i = i + 4
        l = l + 1

    col = 0

    pile_array = []

    while col < len(stack_array[0]):
        pile_array.append([])
        l = len(lines) - 2
        while l >= 0:
            if stack_array[l][col] == "   ":
                break
            pile_array[col].append(stack_array[l][col])
            l = l - 1
        col = col + 1

    ##print(pile_array)

    ##print(move_crate(pile_array,0,1))
    with open('data.txt') as g:
        moves = g.read().splitlines()
        print(moves[0].split())
        for move in moves:
            move_array = move.split()
            iteration = int(move_array[1])
            start = int(move_array[3])
            end = int(move_array[5])


            pile_array = move_crates(pile_array,iteration,start -1,end -1)

        
        print(pile_array)
        result = "x"
        for pile in pile_array:
            result = result + pile[len(pile)-1]

        print(result)






