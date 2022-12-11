#https://www.codewars.com/kata/5e95b6e90663180028f2329d

from collections import defaultdict
from preloaded import only_show_wrong
only_show_wrong()

OFFSETS = {
    "^": [-1, 0],
    "v": [ 1, 0],
    "<": [ 0,-1],
    ">": [ 0, 1]
}

def rpg(field, actions):
    board = [list(row) for row in field]
    hp, atk, defense = 3, 1, 1
    bag = []
    merchants = defaultdict(lambda: 3)
    demon_lord_hp = 10
    xp = 0
    try:
        for action in actions:
            print("\n".join("*%s*" % "".join(row) for row in board) + "\n")
            can_be_attacked = False
            pr = [any(x in row for x in "^v<>") for row in board].index(True)
            pc = [any(c == x for x in "^v<>") for c in board[pr]].index(True)
            if action in "^>v<":
                can_be_attacked = True
                board[pr][pc] = action
            elif action == "F":
                can_be_attacked = True
                player = board[pr][pc]
                fr, fc = OFFSETS[player]
                nr, nc = pr + fr, pc + fc
                if nr < 0 or nc < 0: return None
                next_tile = board[nr][nc]
                if next_tile in "#M-|ED":
                    return None
                if next_tile in "CKH": bag.append(next_tile)
                if next_tile == "S": defense += 1
                if next_tile == "X": atk += 1
                board[pr][pc] = " "
                board[nr][nc] = player
            elif action == "A":
                can_be_attacked = True
                player = board[pr][pc]
                fr, fc = OFFSETS[player]
                nr, nc = pr + fr, pc + fc
                if nr < 0 or nc < 0: return None
                next_tile = board[nr][nc]
                if next_tile not in "ED": return None
                if next_tile == "E":
                    board[nr][nc] = " "
                    xp += 1
                    if xp == 3:
                        xp = 0
                        atk += 1
                if next_tile == "D":
                    demon_lord_hp -= atk
                    if demon_lord_hp <= 0:
                        board[nr][nc] = " "
            elif action in "CKH":
                if action not in bag: return None
                if action == "H":
                    if hp == 3: return None
                    can_be_attacked = True
                    hp = 3
                else:
                    player = board[pr][pc]
                    fr, fc = OFFSETS[player]
                    nr, nc = pr + fr, pc + fc
                    if nr < 0 or nc < 0: return None
                    next_tile = board[nr][nc]
                    if action == "C":
                        if next_tile != "M": return None
                        merchants[(nr, nc)] -= 1
                        if not merchants[(nr, nc)]:
                            board[nr][nc] = " "
                    if action == "K":
                        if next_tile not in "-|": return None
                        board[nr][nc] = " "
                bag.remove(action)
            if can_be_attacked:
                for fr, fc in OFFSETS.values():
                    try: enemy = board[pr + fr][pc + fc]
                    except IndexError: continue
                    if pr + fr < 0: continue
                    if pc + fc < 0: continue
                    if enemy not in "ED": continue
                    dmg = (2 if enemy == "E" else 3) - defense
                    if dmg < 0: continue
                    hp -= dmg
                if hp <= 0: return None
        return board, hp, atk, defense, sorted(bag)
    except:
        return None