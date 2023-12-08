def priority(a:str):
    ascii_v = ord(a)
    if ascii_v >= 97:
        return ascii_v - 96
    else:
        return ascii_v - 64 + 26



with open('data.txt') as f:
    lines = f.read().splitlines()

    sum_priority = 0



    for line in lines:
        compart1 = line[:len(line)//2]
        compart2 = line[len(line)//2:]
        item = "zero"

        for letter in compart1:
            if compart2.find(letter) > -1:
                item = letter
                break
        
        sum_priority = sum_priority + priority(item)
        
    print(sum_priority)

