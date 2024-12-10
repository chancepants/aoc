# with open("day10.in", "r") as fin:
with open("day10.example", "r") as fin:
    GRAPH = [[int(c) for c in line.strip()] for line in fin.readlines()]

N = len(GRAPH)
M = len(GRAPH[0])

def dfs(r,c,g,seen):
    if g[r][c] == 9 and (r,c) not in seen:
        seen.add((r,c))
        return 1
    res = 0
    for dr,dc in ((1,0), (-1,0), (0,1), (0,-1)):
        nr = r + dr
        nc = c + dc
        if nr >= 0 and nr < N and nc >= 0 and nc < M and g[nr][nc] == g[r][c] + 1:
            res += dfs(nr,nc,g,seen)
    return res

def dfs2(r,c,g):
    if g[r][c] == 9:
        return 1
    res = 0
    for dr,dc in ((1,0), (-1,0), (0,1), (0,-1)):
        nr = r + dr
        nc = c + dc
        if nr >= 0 and nr < N and nc >= 0 and nc < M and g[nr][nc] == g[r][c] + 1:
            res += dfs2(nr,nc,g)
    return res

def p1(g: list[list[int]]):
    ans = 0
    for i in range(N):
        for j in range(M):
            if g[i][j] == 0:
                ans += dfs(i,j,g,set())
    print(ans)


def p2(g: list[list[int]]):
    ans = 0
    for i in range(N):
        for j in range(M):
            if g[i][j] == 0:
                ans += dfs2(i,j,g)
    print(ans)


p1(GRAPH)
p2(GRAPH)
