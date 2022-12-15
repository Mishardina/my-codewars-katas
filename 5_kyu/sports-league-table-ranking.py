#https://www.codewars.com/kata/5e0baea9d772160032022e8c

def set_row(v):
    home, away, gHm, gAw = tuple(v)
    table[home] += round((2 if gHm > gAw else 0 if gHm < gAw else 1) * 1e6 + (gHm - gAw) * 1e3 + gHm)
    table[away] += round((2 if gHm < gAw else 0 if gHm > gAw else 1) * 1e6 + (gAw - gHm) * 1e3 + gAw)

def compute_ranks(number, games):
    global table
    
    table = dict.fromkeys(range(number))
    for x in table:    table[x] = 0
    for v in games:    d = set_row(v)

    rank = sorted(list(table.items()), key = lambda i: i[1], reverse = True)
    place = list([x for x in rank])
    
    result = []
    for i, (pos, pts) in enumerate(place):        
        try:    prev = place[i-1:i][0][1]
        except: prev = None
        if  pts != prev:    result.append((i+1, pos))
        elif pts == prev:   result.append((result[i-1][0], pos))
            
    result.sort(key = lambda i: i[1])
    return [x[0] for x in result]