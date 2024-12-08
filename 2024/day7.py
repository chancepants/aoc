OPERATORS: list[tuple[int, list[int]]] = []

# with open("day7.example", "r") as fin:
with open("day7.in", "r") as fin:
    lines = fin.readlines()
    for line in lines:
        res, rest = line.split(":")
        rest = rest.split()
        OPERATORS.append((int(res), [int(op) for op in rest]))


# print(OPERATORS)


def compute(res, ops, i, sm):
    if i == len(ops):
        return sm == res 
    can = False
    can = can or compute(res, ops, i+1, sm + ops[i])
    can = can or compute(res, ops, i+1, sm * ops[i])
    can = can or compute(res, ops, i+1, int(str(sm) + str(ops[i])))
    return can

def p1(ops_lst: list[tuple[int, list[int]]]):
    ans = 0
    for opl in ops_lst:
        res, ops = opl 
        if compute(res, ops, 0, 0):
            ans += res
    print(ans)

def p2():
    pass

p1(OPERATORS)
p2()
