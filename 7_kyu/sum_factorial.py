#https://www.codewars.com/kata/56b0f6243196b9d42d000034

def own_factorial(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact

def sum_factorial(lst):
    sum = 0
    for elem in lst:
        sum += own_factorial(elem)
    return sum