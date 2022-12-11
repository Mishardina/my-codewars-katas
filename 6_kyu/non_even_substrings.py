#https://www.codewars.com/kata/59da47fa27ee00a8b90000b4

def solve(s):
    length = len(s)
    count = 0
    
    for i in range(0,length,1):
        temp = ord(s[i]) - ord('0')
        if (temp % 2 != 0):
            count += (i + 1)
    
    return count