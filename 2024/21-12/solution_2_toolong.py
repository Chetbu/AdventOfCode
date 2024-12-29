import math
# import copy
import time


#import operator

from pathlib import Path

script_name = Path(__file__).stem
current_dir = str(Path(__file__).parent)


file_filepath = Path(current_dir, "data.txt")
start_time = time.time()

numeric_keypad = (
        ('7','8','9'),
        ('4','5','6'),
        ('1','2','3'),
        ('#','0','A')
)

directional_keypad = (
        ('#','^','A'),
        ('<','v','>')
)


def calc_move_keypads(start,end, keypad):
    #locate position of starting number/sign and end number/sign
    x = 0
    #print(start, end)
    while x < len(keypad):
        y = 0
        while y < len(keypad[0]):
            if keypad[x][y] == start:
                x_s, y_s = x, y
            if keypad[x][y] == end:
                x_e, y_e = x, y
            y += 1
        x += 1

    #calc moves
    string_input_lr = ""
    #numbers of moves left or right
    n_push_lr = y_e - y_s 
    if n_push_lr < 0:
        #go left
        string_input_lr += '<' * (-n_push_lr)
    elif n_push_lr > 0:
        string_input_lr += '>' * (n_push_lr)
    
    #numbers of moves up or down
    string_input_ud = ""
    n_push_ud = x_e - x_s 
    if n_push_ud < 0:
        #go up
        string_input_ud += '^' * (-n_push_ud)
    elif n_push_ud > 0:
        string_input_ud += 'v' * (n_push_ud)
    
    #test if starting by left_right ends up in a gap
    possible_string_input_arr = []
    if keypad[x_e][y_s] != '#':
        possible_string_input_arr.append(string_input_ud + string_input_lr + 'A')
    if keypad[x_s][y_e] != '#':
        possible_string_input_arr.append(string_input_lr + string_input_ud + 'A')
    return list(set(possible_string_input_arr))

#print(calc_move_keypads('A',0,numeric_keypad))       

def translate_sequence(input_s, keypad):
    start_position = 'A'
    i = 1
    seq = start_position + input_s
    linear_cache = {'A' : [""]}
    while i < len(seq):
        # print(seq[i], seq[:i])
        if not(seq[:i+1] in linear_cache):
            temp_s_arr = calc_move_keypads(seq[i-1], seq[i], keypad)
            #print(seq[i])
            new_res = []
            #print(input_s, i, seq[:i-1], seq[:i])
            for ele in linear_cache[seq[:i]]:
                for ele2 in temp_s_arr:
                    new_res.append(ele + ele2)
            #print('put in cache', seq[:i+1])
            #print(len(new_res))
            linear_cache[seq[:i+1]] = list(set(new_res))

        i += 1
    return linear_cache[seq]

def translate_sequence_cache(input_s, cache, depth):
    start_position = 'A'
    i = 1
    seq = start_position + input_s
    res_s = ''

    while i < len(seq):
        res_s += cache[(seq[i-1], seq[i], depth)]
        i += 1
    return res_s



with open(file_filepath) as f:
    lines = f.read().splitlines()

# print(lines)

#precalculate the moves

#print(precalculate_moves())
cache = {}
def precalculate_moves_directional(cache_d):
    
    possible_inputs = ('<','v','>','^','A')
    for s in possible_inputs:
        for e in possible_inputs:
            res_arr = calc_move_keypads(s,e, directional_keypad)
            init_res_arr = list(res_arr)

            #evaluate the most efficient
            score_arr = []
            i_max = 3
            for seq in res_arr:
                i = 0
                eval_arr = [seq]
                while i < i_max:
                    res2_arr = []
                    for ele in eval_arr:
                        res2_arr += translate_sequence(ele, directional_keypad)
                    #take only the shorter ones
                    len_arr= [len(x) for x in res2_arr]
                    restricted_res2_arr = [x for x in res2_arr if len(x) == min(len_arr)]

                    eval_arr = restricted_res2_arr
                    i += 1
                score_arr.append(len(eval_arr[0]))
            
            index_best_move = score_arr.index(min(score_arr))
            #print(s, e, init_res_arr, score_arr, init_res_arr[index_best_move])
            cache_d[(s,e,1)] = init_res_arr[index_best_move]
    return cache_d

def precalculate_moves_numeric(cache_d): 
    possible_inputs = ('0','1','2','3','4','5','6','7','8','9','A')
    for s in possible_inputs:
        for e in possible_inputs:
            res_arr = calc_move_keypads(s,e, numeric_keypad)
            init_res_arr = list(res_arr)

            #evaluate the most efficient
            score_arr = []
            i_max = 3
            for seq in res_arr:
                i = 0
                eval_arr = [seq]
                while i < i_max:
                    res2_arr = []
                    for ele in eval_arr:
                        res2_arr += translate_sequence(ele, directional_keypad)
                    #take only the shorter ones
                    len_arr= [len(x) for x in res2_arr]
                    restricted_res2_arr = [x for x in res2_arr if len(x) == min(len_arr)]

                    eval_arr = restricted_res2_arr
                    i += 1
                score_arr.append(len(eval_arr[0]))
            
            index_best_move = score_arr.index(min(score_arr))
            #print(s, e, init_res_arr, score_arr, init_res_arr[index_best_move])
            cache_d[(s,e,1)] = init_res_arr[index_best_move]

    return cache_d

def precalculate_moves_directional_depth(cache_d, depth, base_step):   
    possible_inputs = ('<','v','>','^','A')
    for s in possible_inputs:
        for e in possible_inputs:
            base_t = (s,e,base_step)
            seq = cache_d[base_t]
            i = 1
            i_max = depth
            while i < i_max:
                seq = translate_sequence_cache(seq, cache, base_step)  
                i += base_step
                #print(i)
            cache_d[(s,e,i)] = seq

    return cache_d

cache  = precalculate_moves_directional(cache)
cache = precalculate_moves_numeric(cache)
cache  = precalculate_moves_directional_depth(cache, 5,1)
#cache  = precalculate_moves_directional_depth(cache, 25,5)

print(cache[('>', '^', 5)])

total_score = 0
for line in lines:
    seq = translate_sequence_cache(line, cache, 1)
    i = 0
    depth = 1
    i_max = 25
    while i < i_max:
        seq = translate_sequence_cache(seq, cache, depth)  
        i += depth
        print(i)
    #print(list(set(sequence_arr)))

    m_l_s3 = len(seq)
    print(m_l_s3)
    score = m_l_s3 * int(line[:-1])
    total_score += score

print(total_score, time.time() - start_time)