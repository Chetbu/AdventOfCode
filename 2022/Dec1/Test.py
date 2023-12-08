with open('data.txt') as f:
    lines = f.read().splitlines()
    ##print(int(lines[0])+int(lines[1]))
    current_total = 0
    total_list = []
    max_total = 0
    for line in lines:
        if (line == ''):
            total_list.append(current_total)
            current_total = 0
        else:
            current_total = current_total + int(line)
    total_list.sort(reverse=True)

    print(total_list[0] + total_list[1] + total_list[2])    

