

with open('data.txt') as f:
    lines = f.read().splitlines()
    com = lines[0]
    i = 0
    count = 14
    # while i < (len(lines[0]) - 3):
    #     header = com[i:i+19]
    #     if (header.find(header[1]) + header.find(header[2]) + header.find(header[3])) == 6:
    #         break
    #     count = count + 1
    #     i = i + 1
    while i < (len(lines[0]) - 18):
        header = list( dict.fromkeys(com[i:i+14]))
        if(len(header) == 14):
            break
        i = i + 1
    print(i+14)











