#https://www.codewars.com/kata/54a91a4883a7de5d7800009c

def increment_string(strng):
    print(strng)
    if not strng:
        return str(1)

    if strng.isnumeric():
        return str(int(strng) + 1).zfill(len(strng))

    last_symb = strng[-1]
    if not last_symb.isnumeric():
        return strng + str(1)
    
    incremented_num = 1
    end_num = ''
    i = len(strng) - 1
    while i > 0 and strng[i].isnumeric():
        end_num = strng[i] + end_num
        i -= 1
    end_num = str(int(end_num) + 1).zfill(len(strng) - i - 1)
    
    return strng[:i+1] + end_num