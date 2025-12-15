from __future__ import annotations
import math
from functools import cache

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

with open("day10.ex", "r") as fin:
    LINES = [l.strip() for l in fin.readlines()]
    MACHINES = [Machine.from_line(line=line) for line in LINES]

mx = 0
for m in MACHINES:
    print(m.state, m.buttons, m.joltage)
    mx = max(mx, len(m.state))
print(mx)

def p1():
    @cache
    def solve(m: Machine, c: tuple[bool, ...]) -> int | float:
        # TODO: need to select next button in recursion based on whether it does something to change the state in a positive way
        # otherwise we just keep toggling the same things over and over again flipping between states
        if c == m.state:
            return 0
        mn = math.inf
        for b in m.buttons:
            nc = [False for _ in range(len(c))]
            for k in b:
                nc[k] = not c[k]
            mn = min(mn, 1 + solve(m, tuple(nc)))
        return mn

    sm = 0 
    for mch in MACHINES:
        sm += solve(mch, tuple([False for _ in range(len(mch.state))]))


def p2():
    # dont forget state is mutable between p1 and p2
    pass

p1()
p2()
