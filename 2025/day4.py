with open("day4.in", "r") as fin:
    GRAPH = [[b for b in line.strip()] for line  in fin.readlines()]
M = len(GRAPH)
N = len(GRAPH[0])

def p1():
    res = 0
    for r in range(M):
        for c in range(N):
            cnt = 0
            if GRAPH[r][c] == "@":
                for dr,dc in ((1,0), (1,1), (0,1), (-1, 0), (-1,-1), (0, -1), (1, -1), (-1, 1)):
                    nr = r + dr
                    nc = c + dc
                    if nr >= 0 and nr < M and nc >= 0 and nc < N:
                        if GRAPH[nr][nc] == "@":
                            cnt += 1
                if cnt < 4:
                    res += 1
    print(res)

def p2():
    graph = [[b for b in l] for l in GRAPH]
    def drop_papers():
        res = 0
        for r in range(M):
            for c in range(N):
                cnt = 0
                if graph[r][c] == "@":
                    for dr,dc in ((1,0), (1,1), (0,1), (-1, 0), (-1,-1), (0, -1), (1, -1), (-1, 1)):
                        nr = r + dr
                        nc = c + dc
                        if nr >= 0 and nr < M and nc >= 0 and nc < N:
                            if graph[nr][nc] == "@":
                                cnt += 1
                    if cnt < 4:
                        graph[r][c] = "." 
                        res += 1
        return res
    sol = 0
    while (ret := drop_papers()) > 0:
        sol += ret
    print(sol)

p1()
p2()
