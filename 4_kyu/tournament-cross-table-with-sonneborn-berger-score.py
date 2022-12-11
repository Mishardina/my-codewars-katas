#https://www.codewars.com/kata/5a392890c5e284a7a300003f

def crosstable(players, results):
    n = len(players)
    
    # calculating
    pts = [sum(s     for  s       in     row       if s != None) for row in results]
    sb  = [sum(s*pts for (s, pts) in zip(row, pts) if s != None) for row in results]
    surnames = [p.split(' ')[1] for p in players]
    
    # sorting
    table = zip(range(n), players, pts, sb, surnames)
    table = sorted(table, key = lambda l: (-l[2], -l[3], l[4]))
    ind, players, pts, sb, surnames = zip(*table)
    dict = {None:' ', 0:'0', 0.5:'=', 1:'1'}
    results = [[dict[results[i][j]] for i in ind] for j in ind]
    
    # ranking
    rank = ['1']
    for i in range(1, n):
        same = (pts[i] == pts[i-1] and sb[i] == sb[i-1])
        rank += [' '] if same else [str(i+1)]

    #formating
    header = ['#', 'Player', 'Pts', 'SB'] + [str(x+1) for x in range(n)]
    pts = [f"{x:.1f}" for x in pts]
    sb  = [f"{x:.2f}" for x in sb]
    out = list(zip(rank, players, pts, sb, *results))
        
    w = [max( len(out[i][j]) for i in range(n) ) for j in range(4)] + [len(str(n))]
    form = "{o[0]:>{w[0]}}  {o[1]:<{w[1]}}  "                          \
       + " ".join("{o[" + str(i+4) + "]:>{w[4]}}" for i in range(n))  \
       + "  {o[2]:^{w[2]}}  {o[3]:^{w[3]}}"

    header = form.format(o=header, w=w)
    out = [header.rstrip()]                                      \
        + ['=' * len(header)]                                    \
        + [form.replace("^", ">").format(o=o, w=w) for o in out]
    return '\n'.join(out)