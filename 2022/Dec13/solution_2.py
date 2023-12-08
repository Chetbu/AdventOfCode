
import ast

def arr_eval(line):
    if line == "Correct" or line == "Incorrect":
        return line
    elif len(line) > 0:
        return ast.literal_eval(line)
    else:
        return line
def type(el):
    if isinstance(el,list):
        return "list"
    elif isinstance(el,int):
        return "int"
    else:
        print("alarm")
        return "other"

def compare(list1:list, list2:list):
    max_i = min(len(list1),len(list2))
    #print("max_i is", max_i)
    
    
    if max_i == 0:
        if len(list1) == len(list2):
            return 0        
        elif len(list1) == 0:
            return 1
        else:
            return -1

    else:

        i = 0
        res = 0

        while i < max_i and res == 0:

            #print(list1[i], " vs ", list2[i])


            if type(list1[i]) == "list" and type(list2[i]) == "list": #if both are list
                res = compare(list1[i], list2[i])
            # elif type(list1[i]) == "list":
            #     res = compare(list1[i][0], list2[i])
            # elif type(list2[i]) == "list":
            #     res = compare(list1[i], list2[i][0])

            else:
                res = compare_el(list1[i],list2[i]) 
                #print("result is :", res)            

            i = i + 1

        if res == 0 and len(list1) > len(list2):
            return -1
        elif res == 0 and len(list1) < len(list2):
            return 1
        else:
            return res

def compare_el(left, right):
    #print("el", left, " vs ", right)
    if type(left) == "int" and type(right) == "int":
        if left == right:
            return 0
        elif left < right:
            return 1
        else:
            return -1
    elif type(left) != "int" and len(left) == 0:
        return 1
    elif type(right) != "int" and len(right) == 0:
        return -1
    elif type(left) == "int" and len(right) > 0:
        if type(right[0]) != "int":
            return compare_el(left, right[0])
        elif left == right[0] and len(right) == 1:
            return 0
        elif left <= right[0]:
            return 1
        else:
            return -1
    elif type(right) == "int" and len(left) > 0:
        if type(left[0]) != "int":
            return compare_el(left[0], right)
        elif left[0] < right:
            return 1
        elif left[0] == right and len(left) == 1:
            return 0
        else:
            return -1


   

with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_eval,lines))

    com  = [x for x in lines_array if x != ""]
    com.append([[2]])
    com.append([[6]])

    j = 24

    #print(com[7], "vs", com[j+1])
    # dummy1 = [[[[10, 7, 1, 8], 8, [], 1], 4, 10, 2], [[[9, 3, 10]], 5, [[3, 5], [4], []]], [1]]
    # dummy2 = [[10, [[8, 10, 4]], 9, []], [], [[10], 7], [3, 4, 5, 10, [[6, 4, 8, 7, 9], 3, [0, 5]]]]
    # print("1 vs 2 =", compare(dummy1,dummy2))
    # print("2 vs 1 =",compare(dummy2,dummy1))

    count = 0
    com_not_sorted = True
    while com_not_sorted and count < 5000:
        com_not_sorted = False
        count = count + 1
        
        i = 0
        while i < len(com) - 1:
            if compare(com[i],com[i+1]) != -compare(com[i+1],com[i]):
                print(com[i], "vs", com[i+1])
                print(i)
                break
            if compare(com[i],com[i+1]) == -1:
                #print(com[i], "vs", com[i+1])
                mem = com[i]
                com[i] = com[i+1]
                com[i+1] = mem
                com_not_sorted = True
            i = i + 1

    print(com_not_sorted)
    key = 1
    i = 0
    while i < len(com):
        if com[i] == [[2]] or com[i] == [[6]]:
            key = key * (i+1)
        i = i + 1
    
    print(key)






    

   