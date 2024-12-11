import copy
from collections import defaultdict

with open("day11.in", "r") as fin:
    # with open("day11.example", "r") as fin:
    STONES = fin.readline().strip().split()


def p1(stones: list[str]):
    for _ in range(25):
        nstones = []
        while stones:
            s = stones.pop()
            if s == "0":
                nstones.append("1")
            elif not len(s) % 2:
                s1 = s[: len(s) // 2]
                s2 = s[len(s) // 2 :]
                s2 = s2.lstrip("0")
                if not s2:
                    s2 = "0"
                nstones.append(s1)
                nstones.append(s2)
            else:
                nstones.append(str(int(s) * 2024))
        stones = nstones
    print(len(stones))


def p2(stones: list[str]):
    m = defaultdict(int)
    for s in stones:
        m[s] += 1
    for _ in range(75):
        nm = defaultdict(int)
        for k in m:
            if k == "0":
                nm["1"] += m[k]
            elif not len(k) % 2:
                s1 = k[: len(k) // 2]
                s2 = k[len(k) // 2 :]
                s2 = s2.lstrip("0")
                if not s2:
                    s2 = "0"
                nm[s1] += m[k]
                nm[s2] += m[k]
            else:
                nm[(str(int(k) * 2024))] += m[k]
        m = nm
    print(len(m))
    print(max(m))
    print(sum(m.values()))


p1(copy.copy(STONES))
print("======")
p2(copy.copy(STONES))
