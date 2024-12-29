import math
# import copy
import time
import functools

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

linear_cache = {'A' : [""]}

@functools.cache
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
    return possible_string_input_arr

#print(calc_move_keypads('A',0,numeric_keypad))       

def translate_sequence(input_s, keypad, linear_cache):
    start_position = 'A'
    i = 1
    seq = start_position + input_s
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
            linear_cache[seq[:i+1]] = list(set(new_res))

        i += 1
    return linear_cache, linear_cache[seq]

#print(translate_sequence('029A', numeric_keypad))
#print(translate_sequence('<A^A>^^AvvvA', directional_keypad))

with open(file_filepath) as f:
    lines = f.read().splitlines()

print(lines)
total_score = 0
for line in lines:
    linear_cache, sequence1_arr = translate_sequence(line, numeric_keypad, linear_cache)
    print(linear_cache.keys())
    print(linear_cache['A129A'])
    sequence2_arr = []
    sequence3_arr = []
    for s1 in sequence1_arr:
        linear_cache, sequence2 = translate_sequence(s1, directional_keypad, linear_cache)
        sequence2_arr += sequence2

    print('seq2', linear_cache.keys())

    for s2 in sequence2_arr:

            linear_cache, sequence3 = translate_sequence(s2, directional_keypad, linear_cache)
            sequence3_arr+= sequence3
    print([len(x) for x in sequence3_arr])
    m_l_s3 = min([len(x) for x in sequence3_arr])
    score = m_l_s3 * int(line[:-1])
    total_score += score

print(total_score)