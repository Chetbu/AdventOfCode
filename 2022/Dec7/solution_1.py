def total_dir_size(arr, starting_index:int):
    i = starting_index
    size = 0
    depth = 1
    while i < len(arr) and depth>0:
        if arr[i][0] == "$" and len(arr[i]) == 3:
            if arr[i][2] == "..":
                depth = depth - 1
            else:
                depth = depth + 1
        elif arr[i][0] != "dir" and arr[i][0] != "$":
            ##print(arr[i])
            size = size + int(arr[i][0])



        i = i + 1
    return size

def arr_split(arr):
    return arr.split()

def couple_size(arr):
    return arr[1]

with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_split,lines))

    result_array = []

    i = 0
    while i < len(lines_array):
        if len(lines_array[i]) == 3 and lines_array[i][2] != "..":
            result_array.append([lines_array[i][2],total_dir_size(lines_array,i+1)])
        i = i + 1
    
    ##print(result_array)
    size_array = list(map(couple_size,result_array))

    total_used_space = size_array[0]

    size_array.sort()

    print(size_array)

    # total_size = 0
    # i=0

    # while size_array[i] <= 100000:

    #     total_size = total_size + size_array[i]
    #     i = i+1

    # print(total_size)

    ##print(total_used_space)

    needed_space = 30000000 - 70000000 + total_used_space
    print(needed_space)
    
    i = 0
    while size_array[i] < needed_space:
        i = i + 1
    
    print(size_array[i])


    
    












