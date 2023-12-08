
with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(list,lines))

    #print(lines_array)

    start = [-1,0]
    end = [-1,0]

    i = 0
    j = 0

    step_array = []


    while i < len(lines_array):
        step_array.append([])
        j = 0
        while j < len(lines_array[i]):
            step_array[i].append(-1)

            if lines_array[i][j] == "S":
                start = [i,j]
                lines_array[i][j] = ord("a") - 1
            elif lines_array[i][j] == "E":
                end = [i,j]
                lines_array[i][j] = ord("z") + 1
            else:
                lines_array[i][j] = ord(lines_array[i][j])
            j = j + 1
        i = i + 1
    
    move_backlog = [start]


    step_array[start[0]][start[1]] = 0


    number_step = 0

    while len(move_backlog)>0:
        c_cell = move_backlog[0] #select the cell we want to study
        move_backlog.pop(0) #delete it from the backlog

        cell_value = step_array[c_cell[0]][c_cell[1]] #get the value of the cell
        cell_height = lines_array[c_cell[0]][c_cell[1]] #get heigh of the cell
        
        #test surronding cells if fit

        if c_cell[0] > 0 and (lines_array[c_cell[0]-1][c_cell[1]] - cell_height)<=1 and step_array[c_cell[0]-1][c_cell[1]] < 0: ## if it can go up and not visited
  
            step_array[c_cell[0]-1][c_cell[1]] = cell_value + 1 #set the value
            move_backlog.append([c_cell[0]-1,c_cell[1]])

        if c_cell[0] < len(step_array)-1 and (lines_array[c_cell[0]+1][c_cell[1]] - cell_height)<=1 and step_array[c_cell[0]+1][c_cell[1]] < 0: ## if it can go down and not visited
  
            step_array[c_cell[0]+1][c_cell[1]] = cell_value + 1 #set the value
            move_backlog.append([c_cell[0]+1,c_cell[1]])

        if c_cell[1] > 0 and (lines_array[c_cell[0]][c_cell[1]-1] - cell_height)<=1 and step_array[c_cell[0]][c_cell[1]-1] < 0: ## if it can go left and not visited
  
            step_array[c_cell[0]][c_cell[1]-1] = cell_value + 1 #set the value
            move_backlog.append([c_cell[0],c_cell[1]-1])

        if c_cell[1] < len(step_array[0])-1 and (lines_array[c_cell[0]][c_cell[1]+1] - cell_height)<=1 and step_array[c_cell[0]][c_cell[1]+1] < 0: ## if it can go right and not visited
  
            step_array[c_cell[0]][c_cell[1]+1] = cell_value + 1 #set the value
            move_backlog.append([c_cell[0],c_cell[1]+1])

        number_step = number_step + 1

    
    
    # i = ord("a")
    # min_step_end = 0
    # found_one = True
    # while found_one:
    #     min_step = 10000

    #     found_one = False
    #     x = 0
    #     while x < len(step_array):
    #         y = 0
    #         while y < len(step_array[0]):
    #             if lines_array[x][y] == i and step_array[x][y] > 0:
    #                 found_one = True
    #                 min_step = min(step_array[x][y], min_step)

    #             y = y + 1
    #         x = x + 1
    #     if found_one:
    #         min_step_end = min_step
    #     i = i + 1
    # print(min_step_end)
    # print(i)
    # print(ord("j"))

        






   