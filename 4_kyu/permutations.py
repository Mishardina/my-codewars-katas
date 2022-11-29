#https://www.codewars.com/kata/5254ca2719453dcc0b00027d

from collections import Counter
from math import factorial, prod

def permutations(s):
    if len(s) == 1:
        return [s]
    list_s = list(s)
    list_s = sorted(list_s)
    first_perm = "".join([chr for chr in list_s])
    perms = [first_perm]
    number_of_perms = int(factorial(len(s))/prod(map(factorial, Counter(list_s).values())))
    print(number_of_perms)
    
    for k in range(0, number_of_perms):
        last_perm = list(perms[-1])
                                           
        i = len(last_perm) - 1
        while i > 0 and last_perm[i-1] >= last_perm[i]:
            i -= 1
        if i <= 0:
            continue

        j = len(last_perm) - 1

        while last_perm[j] <= last_perm[i-1]:
            j -= 1

        last_perm[i-1], last_perm[j] = last_perm[j], last_perm[i-1]

        j = len(last_perm) - 1
        while i < j:
            last_perm[i], last_perm[j] = last_perm[j], last_perm[i]
            i += 1
            j -= 1

        new_perm = "".join([chr for chr in last_perm])
        if new_perm not in perms:
            perms.append(new_perm)
            
    return perms