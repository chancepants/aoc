
with open("day4.in", "r") as fin:
# with open("day4.example", "r") as fin:
    grid = [[c for c in line] for line in fin.readlines()]

mp = {
        "X": "M",
        "M": "A",
        "A": "S"
    }


def p1(g):
    N = len(g)
    M = len(g[0])
    def dfs2(r,c, dr, dc):
        if g[r][c] == "S":
            return 1
        nr = r + dr
        nc = c + dc
        ans = 0
        if nr >= 0 and nr < N and nc >= 0 and nc < M and g[nr][nc] == mp[g[r][c]]:
            ans += dfs2(nr,nc,dr,dc)
        return ans

    def dfs(r,c):
        ans = 0
        for dr,dc in ((1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,-1), (-1, 1)):
            nr = r + dr
            nc = c + dc
            if nr >= 0 and nr < N and nc >= 0 and nc < M and g[nr][nc] == mp[g[r][c]]:
                ans += dfs2(nr,nc,dr,dc)
        return ans
    res = 0
    for i in range(N):
        for j in range(M):
            if g[i][j] == "X":
                t = dfs(i,j)
                res += t
    print(res)


def p2(g):
    def is_mas_left(r,c):
        if (g[r-1][c-1] == "M" and g[r+1][c+1] == "S") or (g[r-1][c-1] == "S" and g[r+1][c+1] == "M"):
            return True
    def is_mas_right(r,c):
        if (g[r-1][c+1] == "M" and g[r+1][c-1] == "S") or (g[r-1][c+1] == "S" and g[r+1][c-1] == "M"):
            return True

    def is_xmas(r,c):
        if r >= 1 and r < N-1 and c >= 1 and c < N-1:
            return 1 if is_mas_left(r,c) and is_mas_right(r,c) else 0
        return 0

    N = len(g)
    M = len(g[0])
    ans = 0
    for i in range(N):
        for j in range(M):
            if g[i][j] == "A":
                ans += is_xmas(i,j)
    print(ans)


p1(grid)
p2(grid)

