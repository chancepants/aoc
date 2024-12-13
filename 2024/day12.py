import copy
import itertools
from math import inf

with open("day12.in", "r") as fin:
    # with open("day12.example", "r") as fin:
    # with open("day12.example2", "r") as fin:
    # with open("day12.example3", "r") as fin:
    GRAPH = [[c for c in line.strip()] for line in fin.readlines()]

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def p1(g: list[list[str]]):
    N = len(GRAPH)
    M = len(GRAPH[0])
    seen = set()

    def bfs(r, c):
        perimeter = 0
        area = 0
        q = [(r, c)]
        v = g[r][c]
        seen.add((r, c))
        while q:
            r, c = q.pop()
            area += 1
            for dr, dc in DIRS:
                nr = r + dr
                nc = c + dc
                if (
                    nr >= 0
                    and nr < N
                    and nc >= 0
                    and nc < M
                    and (nr, nc) not in seen
                    and g[nr][nc] == v
                ):
                    q.append((nr, nc))
                    seen.add((nr, nc))
                elif nr < 0 or nr >= N or nc < 0 or nc >= M or g[nr][nc] != v:
                    perimeter += 1
        return area * perimeter

    ans = 0
    for i in range(N):
        for j in range(M):
            if (i, j) not in seen:
                ans += bfs(i, j)
    print(ans)


def get_sides(g: list[list[str]], shape: set[tuple[int, int]]) -> int:
    mnr, mnc = inf, inf
    mxr, mxc = -inf, -inf
    for r, c in shape:
        mnr = min(mnr, r)
        mnc = min(mnc, c)
        mxr = max(mxr, r)
        mxc = max(mxc, c)
    col_edges = []
    row_edges = []
    parity = False
    for r in range(len(g)):
        parity = False
        for c in range(len(g[r])):
            nxt = (r, c) in shape
            if parity != nxt:
                parity = nxt
                col_edges.append((r, c, parity))
    for c in range(len(g[0])):
        parity = False
        for r in range(len(g)):
            nxt = (r, c) in shape
            if parity != nxt:
                parity = nxt
                row_edges.append((r, c, parity))
    sides = 0
    col_edges.sort(key=lambda x: (x[1], x[2]))
    row_edges.sort(key=lambda x: (x[0], x[2]))
    for _, col_group in itertools.groupby(col_edges, key=lambda x: (x[1], x[2])):
        col_group = list(col_group)
        sides += 1
        for i in range(1, len(col_group)):
            pr, _, _ = col_group[i - 1]
            r, _, _ = col_group[i]
            if r > pr + 1:
                sides += 1
    for _, row_group in itertools.groupby(row_edges, key=lambda x: (x[0], x[2])):
        row_group = list(row_group)
        sides += 1
        for i in range(1, len(row_group)):
            _, pc, _ = row_group[i - 1]
            _, c, _ = row_group[i]
            if c > pc + 1:
                sides += 1
    return sides


def p2(g: list[list[str]]):
    seen = set()
    g.insert(0, ["1" for _ in range(len(g[0]))])
    g.append(["1" for _ in range(len(g[0]))])
    for r in g:
        r.insert(0, "1")
        r.append("1")
    N = len(g)
    M = len(g[0])

    def bfs(r, c):
        shape = set()
        area = 0
        q = [(r, c)]
        v = g[r][c]
        seen.add((r, c))
        while q:
            r, c = q.pop()
            area += 1
            shape.add((r, c))
            for dr, dc in DIRS:
                nr = r + dr
                nc = c + dc
                if (
                    nr >= 0
                    and nr < N
                    and nc >= 0
                    and nc < M
                    and (nr, nc) not in seen
                    and g[nr][nc] == v
                ):
                    q.append((nr, nc))
                    seen.add((nr, nc))
        sides = get_sides(g, shape)
        return area * sides

    ans = 0
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if (i, j) not in seen:
                ans += bfs(i, j)
    print(ans)


p1(GRAPH)
p2(copy.copy(GRAPH))
