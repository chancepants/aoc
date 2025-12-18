from __future__ import annotations
import math
from functools import cache
import sys
from typing import Callable

sys.setrecursionlimit(2000)

class Machine:
    def __init__(self, state: tuple[bool, ...], buttons: tuple[tuple[int, ...], ...], joltage: tuple[int, ...]):
        self.state = state 
        self.buttons = buttons
        self.joltage = joltage

    @classmethod
    def from_line(cls, line: str) -> Machine:
        f = lambda x: True if x == "#" else False
        slots = line.split()
        state = tuple([f(c) for c in slots[0].strip("[]")])
        jolts = tuple([int(c) for c in slots[-1].strip("{}").split(",")])
        buttons: list[tuple[int, ...]] = []
        for b in slots[1:-1]:
            buttons.append(tuple([int(d) for d in b.strip("()").split(",")]))
        return cls(state=state, buttons=tuple(buttons), joltage=jolts)

with open("day10.in", "r") as fin:
    LINES = [l.strip() for l in fin.readlines()]
    MACHINES = [Machine.from_line(line=line) for line in LINES]

# mx = 0
# for m in MACHINES:
#     print(m.state, m.buttons, m.joltage)
#     for v in m.joltage:
#         mx = max(mx, v)
# print(mx)

def solver(mch: Machine) -> int:
    dp = {}
    def solve(m: Machine, c: tuple[bool, ...], cost: int) -> None:
        if c in dp and cost >= dp[c]:
            return
        dp[c] = cost
        if c == m.state:
            return
        for b in m.buttons:
            nc = [v for v in c]
            for k in b:
                nc[k] = not c[k]
            solve(m, tuple(nc), cost+1)
        return
    solve(mch, tuple([False for _ in range(len(mch.state))]), 0)
    return dp[mch.state]

def p1():
    sm = 0 
    for mch in MACHINES:
        res = solver(mch)
        sm += res
    print(sm)


def get_buttons(mch: Machine, c: tuple[int, ...], jolt: int) -> list[tuple[int, ...]]:
    nonzero: Callable[[tuple[int, ...]], bool] =  lambda b: all(c[k] for k in b)
    contains_jolt: Callable[[tuple[int, ...]], bool] = lambda b: jolt in b
    return sorted(list(filter(lambda b: nonzero(b) and contains_jolt(b), mch.buttons)), key=lambda b: len(b), reverse=True)

def smallest_jolt(c: tuple[int, ...]) -> tuple[int, int]:
    mn = 100_000 
    mni = -1
    for i,x in enumerate(c):
        if x and x < mn: 
            mn = x
            mni = i
    return mni,mn 


def jolt_solve(mch: Machine) -> int | float:
    # filter out buttons that hit zero joltages
    # pick the lowest value joltage
    # pick the largest button set containing that lowest value joltage
    # increase count by lowest val joltage and reduce all vals in button set
    # loop
    @cache
    def solve(c: tuple[int, ...]) -> int | float:
        if not any(x for x in c):
            return 0
        ret = math.inf
        jolt, mn = smallest_jolt(c=c)
        for b in get_buttons(mch=mch, c=c, jolt=jolt):
            # create new jolt arr
            nc = [x for x in c]
            for k in b:
                nc[k] -= mn
            ret = min(ret, mn + solve(c=tuple(nc)))
        return ret

    return solve(mch.joltage)


def p2():
    sm = 0 
    for i,mch in enumerate(MACHINES):
        print(f"Go {i} {mch.joltage}")
        res = jolt_solve(mch)
        print(res)
        sm += res
    print(sm)

# p1()
p2()
