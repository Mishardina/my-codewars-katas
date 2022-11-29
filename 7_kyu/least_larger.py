#https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4

def least_larger(a, i):
    least_idx = -1
    target_num = a[i]
    prev_num = max(a)
    for j in range(0, len(a)):
        if a[j] > target_num:
            curr_num = a[j]
            if curr_num <= prev_num:
                prev_num = a[j]
                least_idx = j
    return least_idx