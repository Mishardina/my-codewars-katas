def switcher(arr):
    codes = {}
    for i in list(map(chr, range(122, 96, -1))):
        codes[str(123-ord(i))] = i
    codes[str(27)] = '!'
    codes[str(28)] = '?'
    codes[str(29)] = ' '
    
    string = []
    for elem in arr:
        string.append(codes[elem])
    return ''.join(string)