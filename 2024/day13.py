from math import inf
from functools import cache

GAMES: list[list[tuple[int,int]]] = []

# with open("day13.in", "r") as fin:
with open("day13.example", "r") as fin:
    lines = [l.strip() for l in fin.readlines()]
    lines = list(filter(lambda x: x, lines))
    for i in range(0,len(lines),3):
        _, _, ax, ay = lines[i].split()
        _, _, bx, by = lines[i+1].split()
        _, px, py = lines[i+2].split()
        a = (int(ax[2:-1]) ,int(ay[2:]))
        b = (int(bx[2:-1]) ,int(by[2:]))
        p = (int(px[2:-1]) ,int(py[2:]))
        GAMES.append([a,b,p])

@cache
def solver(pos, a, b, t, acnt, bcnt):
    posx,posy = pos
    ax,ay = a
    bx,by = b
    if pos == t:
        return acnt * 3 + bcnt
    if acnt > 100 or bcnt > 100:
        return inf
    res = inf
    res = min(res, solver((posx + ax, posy + ay), a, b, t, acnt+1, bcnt))
    res = min(res, solver((posx + bx, posy + by), a, b, t, acnt, bcnt+1))
    return res

@cache
def solver2(pos, a, b, t, acnt, bcnt):
    posx,posy = pos
    ax,ay = a
    bx,by = b
    if (pos[0] and not t[0] % pos[0]) and (pos[1] and not t[1] % pos[1]):
        print((pos[0], pos[1]), (acnt, bcnt), t[0] // pos[0], t[1] // pos[1])
        return acnt * 3 + bcnt
    if acnt > 200 or bcnt > 200:
        return inf
    res = inf
    res = min(res, solver2((posx + ax, posy + ay), a, b, t, acnt+1, bcnt))
    res = min(res, solver2((posx + bx, posy + by), a, b, t, acnt, bcnt+1))
    return res


# 94x + 22y = 8400
# 22y = 94x + 8400
# y = 94/22x + 8400/22

# 32x + 67y = 5400
# 32x + 67*(94x/22 + 8400/22) = 5400

# 94x + 22x = 8400

def p1(games: list[list[tuple[int,int]]]):
    ans = 0
    for game in games:
        a,b,p = game
        res = solver((0,0), a, b, p, 0, 0)
        ans += 0 if res == inf else res
    print(ans)

# OFFSET = 10000000000000
OFFSET = 0 
def p2(games: list[list[tuple[int,int]]]):
    ans = 0
    for game in games:
        a,b,p = game
        p = (p[0] + OFFSET, p[1] + OFFSET) 
        print(p)
        res = solver2((0,0), a, b, p, 0, 0)
        print(res)
        ans += 0 if res == inf else res
    print(ans)


p1(GAMES)
p2(GAMES)
