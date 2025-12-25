from functools import reduce
import itertools
from operator import mul
with open("day12.in", "r") as fin:
    LINES = [l.strip() for l in fin.readlines()]
    GROUPS: list[list[str]] = [[]]
    for l in LINES:
        if not l:
            GROUPS.append([])
        else:
            GROUPS[-1].append(l)

raw_presents = GROUPS[:6]
grids = GROUPS[-1]
GRID_STUFF: list[tuple[int, list[int]]] = []
for g in grids:
    spots = g.split()
    g_size: int = reduce(mul, [int(x) for x in spots[0][:-1].split("x")])
    pres_counts = [int(x) for x in spots[1:]] 
    GRID_STUFF.append((g_size, pres_counts))

PRESENTS = [p[1:] for p in raw_presents]

def p1():
    p_mins = []
    for p in PRESENTS:
        p_min = len([x for x in itertools.chain.from_iterable(p) if x == "#"])
        p_mins.append(p_min)
    pmax = 9
    no,yes,undetermined = 0,0,0
    for sz, p_counts in GRID_STUFF:
        pmn = sum([p_counts[i] * p_mins[i] for i in range(len(p_counts))])
        pmx = sum([p_counts[i] * pmax for i in range(len(p_counts))])
        if sz >= pmx:
            yes += 1
        elif sz < pmn:
            no += 1
        else:
            undetermined += 1
    print(no,yes,undetermined)

p1()
