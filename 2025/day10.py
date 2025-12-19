from __future__ import annotations
import sys
import z3

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

def p2():
    def solve(m: Machine) -> int:
        presses = [z3.Int(str(i)) for i in range(len(m.buttons))]
        opt = z3.Optimize()
        for p in presses:
            opt.add(p >= 0)
        for i,c in enumerate(m.joltage):
            constraints: list[z3.ArithRef] = []
            for j, btn in enumerate(m.buttons):
                if i in btn:
                    constraints.append(presses[j])
            opt.add(sum(constraints) == c)
        opt.minimize(z3.Sum(presses))
        if opt.check() == z3.sat:
            model = opt.model()
            return sum(model[p].as_long() for p in presses)
        raise RuntimeError("Faile to satisfy") 

    res = 0
    for mch in MACHINES:
        res += solve(mch)
    print(res)


# p1()
p2()
