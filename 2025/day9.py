import math

with open("day9.in", "r") as fin:
    LINES = [l.strip() for l in fin.readlines()]
    TILES = [tuple(int(val) for val in line.split(",")) for line in LINES]


def p1():
    n = len(TILES)
    res = 0
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            x,y = TILES[i]
            x2,y2 = TILES[j]
            v = (abs(x-x2)+1) * (abs(y-y2)+1)
            if v == 4733727792:
                cnt += 1
                print(x,y,x2,y2)
            res = max(res, (abs(x-x2)+1) * (abs(y-y2)+1))
    print(res)
    print(cnt)

def p2():
    # 83956 84990 18711 12439
    n = len(TILES)
    res = 0
    G = [["-" for _ in range(100)] for _ in range(100)]
    pc,pr = TILES[-1]
    for c,r in TILES:
        print(pc, c)
        for i in range(pc, c):
            G[r//1_000][i//1_000] = "X"
        for i in range(pr, r):
            G[i//1_000][c//1_000] = "X"

        # if (c//1_000,r//1_000) in ((83956//1_000, 84990//1_000), (18711//1_000,12439//1_000)):
        #     G[r//1_000][c//1_000] = "O"
        # else:
        G[r//1_000][c//1_000] = "#"
        pc,pr = c,r
    for r in G:
        print("".join(r))
    # raycasting algo polygon in polygon
    # even/odd test along the border of each rectangle
    # 10^2*2 combos * 10^5 eval = 10^9?
    # maybe sort combos and go from biggest until one hits maybe helps a bit
    pass

p1()
p2()
