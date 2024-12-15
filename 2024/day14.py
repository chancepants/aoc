import functools
from io import TextIOWrapper
import math
import operator
from typing import Optional

ROBOTS: list[list[tuple[int, int]]] = []
with open("day14.in", "r") as fin:
# with open("day14.example", "r") as fin:
    lines = [l.strip() for l in fin.readlines()]
    for l in lines:
        p, v = l.split()
        px, py = [int(x) for x in p[2:].split(",")]
        vx, vy = [int(x) for x in v[2:].split(",")]
        ROBOTS.append([(px, py), (vx, vy)])


def get_quadrant(px, py, m, n) -> Optional[int]:
    mid_m = math.floor(m / 2)
    mid_n = math.floor(n / 2)
    if py < mid_n and px < mid_m:
        return 0
    elif py < mid_n and px > mid_m:
        return 1
    elif py > mid_n and px < mid_m:
        return 2
    elif py > mid_n and px > mid_m:
        return 3
    else:
        return None


def p1(robots: list[list[tuple[int, int]]], m, n):
    simul = 100
    quadrants = [0 for _ in range(4)]
    for bot in robots:
        pos, vel = bot
        # print(pos, vel)
        px, py = pos
        vx, vy = vel
        vx *= simul
        vy *= simul
        px += vx
        py += vy
        wrapx, remx = divmod(px, m)
        wrapy, remy = divmod(py, n)
        quad = get_quadrant(remx, remy, m, n)
        if quad is not None:
            quadrants[quad] += 1
        # print((remy, remx))
    print(quadrants)
    print(functools.reduce(operator.mul, quadrants))


def simul(robots: list[list[tuple[int,int]]], m, n):
    new_bots = []
    for pos,vel in robots:
        px,py = pos
        vx,vy = vel
        px += vx
        py += vy
        px = px % m
        py = py % n
        new_bots.append([(px,py), (vx,vy)])
    return new_bots

def display_bots(robots: list[list[tuple[int,int]]], g: list[list[str]]) -> list[str]:
    positions = set()
    lines = []
    for pos,_ in robots:
        positions.add(pos)
    for r in range(len(g)):
        for c in range(len(g[r])):
            g[r][c] = "*" if (c,r) in positions else "."
        lines.append("".join(g[r]) + "\n")
    return lines

def p2(robots: list[list[tuple[int, int]]], m, n):
    g = [["." for _ in range(m)] for _ in range(n)]
    display_bots(robots, g)
    with open("day14.out", "w") as fout:
        for i in range(20000):
            robots = simul(robots, m, n)
            fout.write(f"\n========={i+1}=========\n")
            lines = display_bots(robots, g)
            fout.writelines(lines)


p1(ROBOTS, 101, 103)
p2(ROBOTS, 101, 103)
