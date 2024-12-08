from collections import defaultdict


_deps: list[tuple[int,int]] = []
_updates: list[list[int]] = []
with open("day5.in", "r") as fin:
# with open("day5.example", "r") as fin:
    lines = fin.readlines()
    for line in lines:
        if "|" in line:
            x,y = line.split("|")
            _deps.append((int(x), int(y)))
        elif "," in line:
            vals = line.split(",")
            _updates.append([int(v) for v in vals])


def p1(deps, updates):
    g = defaultdict(set) 
    for x,y in deps:
        g[x].add(y)

    def good_update(update):
        for i in range(len(update)):
            for j in range(0, i):
                if update[j] in g[update[i]]:
                    return False
        return True 

    good_updates = []
    for update in updates:
        if good_update(update):
            good_updates.append(update)

    ans = 0
    for update in good_updates:
        ans += update[len(update) // 2]
    print(ans)

def p2(deps, updates):
    g = defaultdict(set) 
    for x,y in deps:
        g[x].add(y)

    def good_update(update):
        for i in range(len(update)):
            for j in range(0, i):
                if update[j] in g[update[i]]:
                    return False
        return True 

    bad_updates = []
    for update in updates:
        if not good_update(update):
            bad_updates.append(update)

    new_goods = []
    for update in bad_updates:
        new_goods.append([])
        m = {} 
        for i in range(len(update)):
            m[update[i]] = 0
            for j in range(len(update)):
                if update[i] in g[update[j]]:
                    m[update[i]] += 1

        while len(new_goods[-1]) < len(update):
            k_rem = None
            print(m)
            for k in m:
                if not m[k]:
                    new_goods[-1].append(k)
                    k_rem = k
                    m.pop(k)
                    break
            for v in g[k_rem]:
                if v in m:
                    m[v] -= 1
        print(new_goods[-1])
        print(m)
    ans = 0
    for goods in new_goods:
        ans += goods[len(goods) // 2]
    print(ans)


p1(_deps, _updates)
p2(_deps, _updates)
