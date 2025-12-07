
from functools import cache


with open("day7.in", "r") as fin:
    LINES = [l.strip("\n") for l in fin.readlines()]
    G = [[c for c in line] for line in LINES]
M = len(G)
N = len(G[0])

def get_s() -> tuple[int,int]:
    for r in range(M):
        for c in range(N):
            if G[r][c] == "S":
                return r,c
    raise RuntimeError

seen = set()
def dfs(r: int, c: int) -> int:
    if G[r][c] not in (".", "S"):
        print(G[r][c],r,c)
        raise RuntimeError
    seen.add((r,c))
    if r == M-1:
        return 0
    res = 0
    if G[r+1][c] == "^":
        res += 1
        for dc in (1,-1):
            nc = c + dc
            if nc >= 0 and nc < N and (r+1, nc) not in seen:
                res += dfs(r+1, nc)
    elif (r+1, c) not in seen:
        res += dfs(r+1, c)
    return res

@cache
def dfs2(r: int, c: int) -> int:
    if G[r][c] not in (".", "S"):
        print(G[r][c],r,c)
        raise RuntimeError
    if r == M-1:
        return 0
    res = 0
    if G[r+1][c] == "^":
        res += 1
        for dc in (1,-1):
            nc = c + dc
            if nc >= 0 and nc < N and (r+1, nc):
                res += dfs2(r+1, nc)
    else:
        res += dfs2(r+1, c)
    return res

def p1():
    sr,sc = get_s()
    print(dfs(sr,sc))


def p2():
    sr,sc = get_s()
    print(dfs2(sr,sc) + 1)


p1()
p2()
