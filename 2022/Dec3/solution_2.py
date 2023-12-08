def priority(a:str):
    ascii_v = ord(a)
    if ascii_v >= 97:
        return ascii_v - 96
    else:
        return ascii_v - 64 + 26



with open('data.txt') as f:
    lines = f.read().splitlines()

    sum_priority = 0

    i = 0
    print(len(lines))



    while i < len(lines):

        item = "zero"

        for letter in lines[i]:
            if lines[i+1].find(letter) > -1 and lines[i+2].find(letter) > -1:
                item = letter
                break
        
        sum_priority = sum_priority + priority(item)
        i = i + 3
        
    print(sum_priority)

