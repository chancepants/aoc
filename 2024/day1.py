

from collections import Counter


with open("day1.in", "r") as fin:
    lines = fin.readlines()
left = []
right = []
for line in lines:
    li, ri = line.split()
    left.append(int(li))
    right.append((int(ri)))

def p1(lft, rht):
    lft = sorted(lft)
    rht = sorted(rht)
    ans = 0
    for i in range(len(lft)):
        ans += abs(lft[i]-rht[i])
    print(ans)

def p2(lft, rht):
    ans = 0
    lcnt = Counter(lft)
    rcnt = Counter(rht)
    for v in lcnt:
        ans += v * lcnt[v] * rcnt.get(v, 0)
    print(ans)

p1(left,right)
p2(left,right)



