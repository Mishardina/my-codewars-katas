#https://www.codewars.com/kata/61711668cfcc35003253180d

def identify_bb(bearings, weigh):
    res = 0 
    b = []
    for i in range(0, len(bearings)):
        for j in range(0, i+1):
            res += 10
            b.append(bearings[i])
    return bearings[(weigh(*b) - res - 1)]