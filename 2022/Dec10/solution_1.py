
def arr_split(arr):
    return arr.split()




with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_split,lines))

    #print(lines_array)

    X = 1

    X_values = [1,1]
    for line in lines_array:
        if len(line) == 1:
            X_values.append(X)
        else:
           X_values.append(X)
           X = X + int(line[1])
           X_values.append(X) 
    #print(X_values)

    i = 20
    sum = 0
    while i < len(X_values):
        sum = sum + i * X_values[i]

        i = i + 40
    #print(sum)

    i = 0
    line_return = 39
    screen = ""
    offset = 0
    while i < len(X_values)-1:
        if abs(X_values[i+1] - i + offset)<=1:
            screen =screen +"#"
        else:
            screen =screen +"."
        if line_return == 0:
            screen = screen + '\n'
            line_return = 40
            offset = offset + 40

        i = i +1
        line_return = line_return - 1
    print(screen)

    


   