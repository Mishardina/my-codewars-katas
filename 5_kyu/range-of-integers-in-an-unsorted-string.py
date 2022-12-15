#https://www.codewars.com/kata/5b6b67a5ecd0979e5b00000e

def mystery_range(s,n):
    for i in range(1,100):
        if sorted(list(s)) == sorted(''.join(map(str,range(i,i+n)))) and str(i) in s:
            return [i,i+n-1]