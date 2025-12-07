
from functools import reduce
from operator import add, mul


with open("day6.in", "r") as fin:
    LINES = [l.strip("\n") for l in fin.readlines()]
    G = [l.split() for l in LINES]

M = len(G)
N = len(G[0])

def p1():
    res = 0
    for c in range(N):
        ops: list[str] = []
        for r in range(M):
            ops.append(G[r][c])
        operands = [int(n) for n in ops[:-1]]
        operator = ops[-1]
        if operator == "+":
            res += sum(operands)
        elif operator == "*":
            res += reduce(mul, operands)
    print(res)


def p2():
    res = 0
    m = len(LINES)
    n = len(LINES[0])
    graph = [["" for _ in range(m)] for _ in range(n)]
    for c in range(n):
        for r in range(m-1):
            graph[c][r] = LINES[r][c]
    nums: list[list[int]] = [[]]
    for row in graph:
        if all(not x.isdigit() for x in row):
            nums.append([])
        else:
            nums[-1].append(int("".join([x for x in row if x.isdigit()])))
    ops = [op for op in LINES[-1].split()]
    mp = {"+": add, "*" : mul}
    for i in range(len(nums)):
        res += reduce(mp[ops[i]], nums[i])
    print(res)


p1()
p2()
