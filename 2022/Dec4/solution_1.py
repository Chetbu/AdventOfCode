def split_couples(a:str):
    return a.split("-")




with open('data.txt') as f:
    lines = f.read().splitlines()

    count = 0

    for line in lines:
        res = list(map(split_couples, line.split(",")))
        zone1 = res[0]
        zone2 = res[1]
        # if int(zone1[0]) <= int(zone2[0]) and int(zone1[1]) >= int(zone2[1]):
        #     ##print(res)

        #     count = count +1
        # elif int(zone1[0]) >= int(zone2[0]) and int(zone1[1]) <= int(zone2[1]):
        #     print(res)

        #     count = count + 1
        if int(zone1[0]) <= int(zone2[0]) and int(zone1[1])>= int(zone2[0]):
            print(res)
            count = count + 1
        elif int(zone2[0]) <= int(zone1[0]) and int(zone2[1])>= int(zone1[0]):
            print(res)
            count = count + 1
    print(count)





