# import math
import copy
import time

def arr_eval(arr):
    return arr.split(" ")

class Ressources:
    def __init__(self, ore:int, clay:int, obsidian:int):
        self.ore:int = ore
        self.clay:int = clay
        self.obs:int = obsidian
        self.geode:int = 0

    def __str__(self):
        return f"ore: {self.ore}, clay: {self.clay}, obs: {self.obs}, geode: {self.geode}"

class Blueprint:
    def __init__(self):
        self.id:int = 0
        self.ore_robot:Ressources
        self.clay_robot:Ressources
        self.obs_robot:Ressources
        self.geode_robot:Ressources

    def __str__(self):
        return f"ore_robot is {self.ore_robot}, clay_robot is {self.clay_robot}, obs_robot is {self.obs_robot} and geode_robot is {self.geode_robot}"

class State:
    def __init__(self):
        self.round:int = 0
        self.res:Ressources = Ressources(0, 0, 0)
        self.ore_robot:int = 1
        self.clay_robot:int = 0
        self.obs_robot:int = 0
        self.geode_robot:int = 0
        self.can_construct:list = [True, True, True, True]

    def __str__(self):
        return f"Round: {self.round}; Ressources : {self.res}; ore_robot :{self.ore_robot}, clay_robot :{self.clay_robot}, obs_robot :{self.obs_robot}, geode_robot :{self.geode_robot}, const :{self.can_construct}"

def gather_ressource(c_s: State):
    c_s.res.clay = c_s.res.clay + c_s.clay_robot
    c_s.res.obs = c_s.res.obs + c_s.obs_robot
    c_s.res.ore = c_s.res.ore + c_s.ore_robot
    c_s.res.geode = c_s.res.geode + c_s.geode_robot
    return c_s

def max_robot_needed(b:Blueprint):
    str_arr = ["ore", "clay", "obs", "geode"]
    i = 0
    res = []
    while i < len(str_arr):
        max_robot = 0
        for s in str_arr:
            max_robot = max(max_robot, getattr(getattr(b, s+"_robot"),str_arr[i]))
        res.append(max_robot)
        i += 1
    return res


def can_construct_new_robot(c_s: State, b:Blueprint, max_array:list): #NEED to block creation of robots when not needed
    str_arr = ["ore", "clay", "obs", "geode"]
    res = []
    for i, s in enumerate(str_arr):
        if (getattr(c_s, s +"_robot") >= max_array[i]) and s != "geode":
            res.append(False)
        else:
            el = True
            r_needs = getattr(b, s +"_robot")
            for t in str_arr:
                if getattr(r_needs, t) > getattr(c_s.res, t):
                    el = False
            res.append(el)
    return [str_arr, res]   

def create_new_robot(c_s: State, b:Blueprint, s:str): 
    str_arr = ["ore", "clay", "obs", "geode"]
    r_needs = getattr(b, s +"_robot")
    attribute = s + "_robot"
    setattr(c_s, attribute, getattr(n_state, attribute) + 1)
    c_s.can_construct = [True, True, True, True]
    for t in str_arr:
        setattr(c_s.res,t,getattr(c_s.res, t) - getattr(r_needs, t)) 

    return  

def esperance(c_s: State, b:Blueprint, max_round:int):
    rem_round = max_round - c_s.round
    #clay_esp = c_s.res.clay + rem_round*(c_s.clay_robot + rem_round - 1) #high scenario where a robot is created every round until the end
    #aff_obs = min((rem_round - 1),int(clay_esp/b.obs_robot.clay))
    aff_obs = (rem_round - 1)
    obs_esp = c_s.res.obs + rem_round*(c_s.obs_robot + aff_obs) #high scenario where a robot is created every round until the end
    
    aff_geo = min((rem_round - 1),int(obs_esp/b.geode_robot.obs))    
    geo_esp = c_s.res.geode + rem_round*(c_s.geode_robot + aff_geo) #high scenario where a robot is created every round until the end
    return geo_esp

def more_ressources(res1: Ressources, res2: Ressources):
    str_arr = ["ore", "clay", "obs", "geode"]
    for s in str_arr:
        if getattr(res2, s) > getattr(res1, s):
            return False
    return True




with open('data.txt') as f:
    lines = f.read().splitlines()
    lines_array = list(map(arr_eval,lines))

    #print(lines_array[0])

    blueprint_arr = []

    for line in lines_array:
        new_blueprint = Blueprint()
        new_blueprint.id = int(line[1][:-1])
        
        new_blueprint.ore_robot = Ressources(int(line[6]),0,0)
        new_blueprint.clay_robot = Ressources(int(line[12]),0,0)
        new_blueprint.obs_robot = Ressources(int(line[18]),int(line[21]),0)
        new_blueprint.geode_robot = Ressources(int(line[27]),0,int(line[30]))

        #print(new_blueprint)
        blueprint_arr.append(new_blueprint)

b_id = 0
product_max_geode = 1
while b_id < min(len(blueprint_arr),3):
    #init 
    start_state = State()

    state_array = [start_state]
    #state_array[0].res.ore = 3
    count = 0
    max_geode = 0
    max_r = 30
    bluepr:Blueprint = blueprint_arr[b_id]

    max_arr = []

    st = time.time()


    # determine the max robots needed for ore
    max_list = max_robot_needed(bluepr)



    #print(c_state)
    while len(state_array) > 0 and count < 10000000:
        count +=1
        c_state = state_array[0]
        c_state.round += 1

        if c_state.round == max_r:
            gather_ressource(c_state)
            if c_state.res.geode > max_geode:
                max_geode = c_state.res.geode
                max_arr = [c_state]

                i = 1

                while i < len(state_array):
                    if esperance(state_array[i], bluepr, max_r) < max_geode:
                        del state_array[i]
                    i += 1
            elif c_state.res.geode == max_geode and max_geode > 0:
                max_arr.append(c_state)

            del state_array[0]

        elif esperance(c_state, bluepr, max_r+1) < max_geode:
            del state_array[0]

        else:
            #check if c_state is better than other waiting state
            i = 1
            # while i < len(state_array):
            #     if is_better(c_state, state_array[i]):
            #         del state_array[i]
            #     i += 1
            new_robots = can_construct_new_robot(c_state,bluepr,max_list) #check if new robot can be build (on old ressources count)
            gather_ressource(c_state) #gather ressources
            i = len(new_robots[0]) - 1
            while i >= 0: #enumarate the robot that can be build
                if new_robots[1][i] and c_state.can_construct[i]:
                    n_state = copy.deepcopy(c_state) ##new state for robot creation
                    # 2 ways / either we build the robot (n_state) or we block the creation until next robot is build in c_state
                    #build new robot in n, and reset the can_construct
                    attr = new_robots[0][i]
                    create_new_robot(n_state, bluepr,attr)
                    

                    #georobot are always the best choice for ressource spending
                    if attr == "geode":
                        del state_array[0]

                    else:
                        #block construction on c_state
                        c_state.can_construct[i] = False

                    #state_array.append(n_state)
                    state_array.insert(0,n_state)

                    

                i = i - 1
    print(max_geode)
     
    print(len(state_array))

    print("End ", time.time() - st)
    b_id += 1
    max_geode_robot = 0
    for s in max_arr:
        max_geode_robot = max(max_geode_robot, s.geode_robot)

    calc_max_geode = max_geode + 2 * max_geode_robot + 3

    print(calc_max_geode)
    
    
    product_max_geode = product_max_geode * calc_max_geode

print(product_max_geode)

# test_s = State()
# test_s.geode_robot = 1


# print(esperance(test_s,blueprint_arr[0],2))
    
# for state in max_arr:
#     print(state)


# for state in state_array:
#     print(state)


