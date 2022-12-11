#https://www.codewars.com/kata/566d5e2e57d8fae53c00000c

import random

def get_bingo_card():
    B_list = random.sample(range(1, 16), 5)
    I_list = random.sample(range(16, 31), 5)
    N_list = random.sample(range(31, 46), 4)
    G_list = random.sample(range(46, 61), 5)
    O_list = random.sample(range(61, 76), 5)
    
    return    ['B' + str(B_list[i]) for i in range(len(B_list))] \
            + ['I' + str(I_list[i]) for i in range(len(I_list))] \
            + ['N' + str(N_list[i]) for i in range(len(N_list))] \
            + ['G' + str(G_list[i]) for i in range(len(G_list))] \
            + ['O' + str(O_list[i]) for i in range(len(O_list))]