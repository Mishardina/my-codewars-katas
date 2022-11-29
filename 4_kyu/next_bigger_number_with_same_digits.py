#https://www.codewars.com/kata/55983863da40caa2c900004e

def next_bigger(n):
    list_n = list(map(int, str(n)))
    print(list_n)
    
    i = len(list_n) - 1
    while i > 0 and list_n[i-1] >= list_n[i]:
        i -= 1
    if i <= 0:
        return -1
    
    j = len(list_n) - 1
    
    while list_n[j] <= list_n[i-1]:
        j -= 1
    
    list_n[i-1], list_n[j] = list_n[j], list_n[i-1]
    
    j = len(list_n) - 1
    while i < j:
        list_n[i], list_n[j] = list_n[j], list_n[i]
        i += 1
        j -= 1
    
    final_n = int("".join([str(integer) for integer in list_n]))
    return final_n