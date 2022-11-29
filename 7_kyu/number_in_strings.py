#https://www.codewars.com/kata/59dd2c38f703c4ae5e000014

def solve(s):
    number = ''
    longest_num = '0'
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = 1
            while s[i:i+j].isdigit() and (i + j-1) < len(s):
                print(i+j)
                number = s[i:i+j]
                print(number)
                j += 1
            if int(number) > int(longest_num):
                longest_num = number
            i += j
        else:
            i += 1
    return int(''.join(longest_num))