from functools import reduce
import heapq
import math
from operator import mul

with open("day8.in", "r") as fin:
    LINES = [l.strip() for l in fin.readlines()]
    BOXES = [tuple(int(val) for val in line.split(",")) for line in LINES]

def dist(b1,b2) -> float:
    x1,y1,z1 = b1 
    x2,y2,z2 = b2 
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

def root(uf,b):
    if uf[b][0] != b:
        return root(uf,uf[b][0])
    return b

def uf_add(uf,b1,b2) -> None:
    b1 = root(uf,b1)
    b2 = root(uf,b2)
    if b1 == b2:
        return
    uf[b1][1] = uf[b1][1] + uf[b2][1]
    uf[b2] = [b1, 1]
    return uf[b1][1]


def p1():
    uf = {box: [box, 1] for box in BOXES}
    distq = []
    for i in range(len(BOXES)):
        for j in range(i+1,len(BOXES)):
            b1 = BOXES[i]
            b2 = BOXES[j]
            if b1 != b2:
                heapq.heappush(distq, (dist(b1,b2), b1, b2))
    for _ in range(1000):
        _,b1,b2 = heapq.heappop(distq)
        uf_add(uf,b1,b2)
    l = sorted(uf.values(), key=lambda x: x[1], reverse=True)
    print(reduce(mul, [p[1] for p in l[:3]]))


def p2():
    uf = {box: [box, 1] for box in BOXES}
    distq = []
    for i in range(len(BOXES)):
        for j in range(i+1,len(BOXES)):
            b1 = BOXES[i]
            b2 = BOXES[j]
            if b1 != b2:
                heapq.heappush(distq, (dist(b1,b2), b1, b2))
    def pick():
        while distq:
            _,b1,b2 = heapq.heappop(distq)
            size = uf_add(uf,b1,b2)
            if size == len(BOXES):
                return size,b1,b2
        raise RuntimeError

    _,r1,r2 = pick()
    print(r1[0] * r2[0])

p1()
p2()
