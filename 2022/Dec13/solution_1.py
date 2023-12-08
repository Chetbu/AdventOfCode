
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
    print("el", left, " vs ", right)
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

    #print(lines_array)
    #print(type(lines_array[2]))
    #print(compare(lines_array[59*3], lines_array[59*3+1]))
    #print(lines_array[18*3])
    i = 0
    index = 1
    index_array = []
    sum = 0
    while i < len(lines_array):
        res = compare(lines_array[i], lines_array[i+1])

        if res == 1:
            sum = sum + index
            index_array.append(index)
        index = index + 1
        i = i + 3
    print(index_array)
    print(sum)



    

   