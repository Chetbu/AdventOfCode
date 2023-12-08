
def arr_split(arr):
    return arr.split()

def inspect(arr):
    return arr.count_inspect

class Monkey:
    def __init__(self):
        self.id = 0
        self.items = []    # creates a new empty list for each monkey
        self.worry_operation = "" #capture the operation ("+", "*", or "^")
        self.worry_factor = 0 #capture the factor
        self.test_factor = 0 #capture the divisibility factor
        self.throw_true = 0
        self.throw_false = 0
        self.count_inspect = 0



with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_split,lines))

    #print(lines_array)

    i = 0
    monkey_count = 0
    monkey_array = []
    while i < len(lines_array):

        current_monkey = Monkey()
        current_monkey.id = monkey_count
        j = 2
        while j < len(lines_array[i + 1]):
            current_item = lines_array[i + 1][j]
            #print(current_item[len(current_item)-1:])
            if current_item[len(current_item)-1:] == ",":
                current_item = current_item[:len(current_item)-1]
            #print(current_item)
            current_monkey.items.append(int(current_item))
            j = j + 1
        if lines_array[i + 2][5] == "old":
            current_monkey.worry_operation = "^"
        else:
            current_monkey.worry_operation = lines_array[i + 2][4]
            current_monkey.worry_factor = int(lines_array[i + 2][5])
        current_monkey.test_factor = int(lines_array[i + 3][3])
        current_monkey.throw_true = int(lines_array[i + 4][5])
        current_monkey.throw_false = int(lines_array[i + 5][5])
        monkey_array.append(current_monkey)

        i = i + 7
        monkey_count = monkey_count + 1

    round_number = 1
    round_limit = 10000

    divider = 1

    for m in monkey_array:
        divider = divider * m.test_factor

    #print(divider)


    while round_number <= round_limit:
        for monkey in monkey_array:
            current_item_list = monkey.items
            monkey.items = []
            for item in current_item_list:
                monkey.count_inspect = monkey.count_inspect + 1
                current_item = item
                if monkey.worry_operation == "+":
                    current_item = current_item + monkey.worry_factor
                elif monkey.worry_operation == "*":
                    current_item = current_item * monkey.worry_factor
                else:
                    current_item = current_item * current_item
                #current_item = int(current_item/3)

                if current_item > divider:
                    current_item = current_item % divider

                #print(current_item)

                if current_item % monkey.test_factor == 0:
                    monkey_array[monkey.throw_true].items.append(current_item)
                else:
                    monkey_array[monkey.throw_false].items.append(current_item)
        round_number = round_number + 1
    

    inspect_array = list(map(inspect,monkey_array))
    inspect_array.sort(reverse=True)
    print(inspect_array[0] * inspect_array[1])





  