#https://www.codewars.com/kata/5a15a4db06d5b6d33c000018

def sum_nested(lst):
    total = 0
    for i in lst:
        if isinstance(i, list):
            total += sum_nested(i)
        else:
            total += i
    return total