import math
with open("day5.in", "r") as fin:
    lines = [l.strip() for l in fin.readlines()]
    FRESH: list[list[int]] = []
    INGREDIENTS: list[int] = []
    s = 0
    for i in range(len(lines)):
        s = i
        if lines[i]:
            FRESH.append([int(c) for c in lines[i].split("-")])
        else: break
    for j in range(s+1, len(lines)):
        INGREDIENTS.append(int(lines[j]))


def collapse_ranges(lst: list[list[int]]) -> list[list[int]]:
    pr = -math.inf 
    nlst: list[list[int]] = []
    for l,r in lst:
        if l <= pr:
            nlst[-1][-1] = max(nlst[-1][-1], r)
        else:
            nlst.append([l,r])
        pr = r
    return nlst


def is_fresh(fresh: list[list[int]], id: int) -> bool:
    # binary search on x[0] is optimal
    for l,r in fresh:
        if id >= l and id <= r:
            return True
    return False


def p1():
    res = 0
    fresh = [[min(l,r), max(l,r)] for l,r in FRESH]
    fresh.sort(key=lambda x: x[0])
    nfresh = collapse_ranges(lst=fresh)
    for id in INGREDIENTS:
        res += int(is_fresh(fresh=nfresh, id=id))
    print(res)


def p2():
    res = 0
    fresh = [[min(l,r), max(l,r)] for l,r in FRESH]
    fresh.sort(key=lambda x: x[0])
    nfresh = collapse_ranges(lst=fresh)
    for l,r in nfresh:
        res += (r-l+1)
    print(res)


p1()
p2()
