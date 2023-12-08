# import math

corresp = (
        ("=","-","0","1","2"),
        (-2,-1,0,1,2)
    )



def eval_1(s:str):

    i = 0
    
    while corresp[0][i] != s:
        i +=1
    return corresp[1][i]

def eval_SNAFU(s:str):
    i = len(s) - 1
    mult = 1
    res = 0
    while i >= 0:
        res += eval_1(s[i]) * mult
        i -= 1
        mult = 5 * mult
    return res

def convert_to_SNAFU(n:int):
    res = []
    mult = 1
    temp = n
    while mult < n:
        mult = 5 * mult
    
    mult = int(mult / 5)

    while mult >= 1:
        # print(temp, mult)

        x = temp // mult        
        res.append(x)        
        temp = temp - x * mult

        mult = int(mult / 5)

    # print(res)

    i = len(res) - 1
    while i > 0:
        if res[i] >= 3:
            res[i] = res[i] - 5
            res[i-1] += 1

        i -= 1

    if res[0] >= 3:
        res[0] = res[0] - 5
        res.insert(0,1)

    s = ""

    for number in res:
        i=0
        while corresp[1][i] != number:
            i +=1
        s += corresp[0][i]
    
    return s



    

    




with open('data.txt') as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    total += eval_SNAFU(line)

print("Total is :", total)
print(convert_to_SNAFU(total))

    