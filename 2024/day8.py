from collections import defaultdict
from itertools import combinations

with open("day8.in", "r") as fin:
    # with open("day8.example", "r") as fin:
    GRID = [[c for c in line.strip()] for line in fin.readlines()]


def p1(grid: list[list[str]]):
    m: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != ".":
                m[grid[r][c]].append((r, c))
    N = len(grid)
    M = len(grid[0])
    pos = set()
    for k in m:
        for s, t in combinations(m[k], 2):
            sr, sc = s
            tr, tc = t
            dr = tr - sr
            dc = tc - sc
            anti_tr = tr + dr
            anti_tc = tc + dc
            anti_sr = sr - dr
            anti_sc = sc - dc
            for ar, ac in ((anti_tr, anti_tc), (anti_sr, anti_sc)):
                if ar >= 0 and ar < N and ac >= 0 and ac < M:
                    pos.add((ar, ac))
    print(len(pos))


def p2(grid: list[list[str]]):
    m: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != ".":
                m[grid[r][c]].append((r, c))
    N = len(grid)
    M = len(grid[0])
    pos = set()
    for k in m:
        for s, t in combinations(m[k], 2):
            sr, sc = s
            tr, tc = t
            dr = tr - sr
            dc = tc - sc
            ar, ac = sr, sc
            while ar >= 0 and ar < N and ac >= 0 and ac < M:
                pos.add((ar, ac))
                ar = ar - dr
                ac = ac - dc
            ar, ac = tr, tc
            while ar >= 0 and ar < N and ac >= 0 and ac < M:
                pos.add((ar, ac))
                ar = ar + dr
                ac = ac + dc
    print(len(pos))


p1(GRID)
p2(GRID)
