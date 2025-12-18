from functools import cache


with open("day11.in", "r") as fin:
    LINES = [l.strip() for l in fin.readlines()]
    D = {}
    for l in LINES:
        n, vtxs = l.split(":")
        D[n] = vtxs.split()


def p1():
    @cache
    def dfs(v: str):
        if v == "out":
            return 1
        res = 0
        for n in D[v]:
            res += dfs(n)
        return res
    print(dfs("you"))

def p2():
    @cache
    def dfs(v: str, dac: bool, fft: bool):
        if v == "out":
            if dac and fft:
                return 1
            return 0
        if v == "dac":
            dac = True
        if v == "fft":
            fft = True
        res = 0
        for n in D[v]:
            res += dfs(n, dac=dac, fft=fft)
        return res
    print(dfs("svr", False, False))

# p1()
p2()
