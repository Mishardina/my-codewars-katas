#https://www.codewars.com/kata/57b4d2dad2a31c75f7000223

def get_number_of_reachable_fields(a, rows, cols, sx, sy):
    q = [(sx, sy)]
    for x, y in q:
        for dx, dy in ((1, 0), (0, -1), (0, 1)):
            X, Y = x + dx, y + dy
            if 0 <= X < rows and 0 <= Y < cols and a[X][Y] == 1:
                a[X][Y] = 2
                q.append((X, Y))
    return a[-1].count(2)