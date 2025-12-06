with open("day1.in", "r") as fin:
    OPERATIONS = [(-1 if line[0] == "L" else 1, int(line[1:])) for line in fin.readlines()]

MOD = 100

def p1():
    res = 0
    pos = 50
    for dir, count in OPERATIONS:
        pos = (pos + (dir*count)) % MOD
        if not pos:
            res += 1
    print(res)

def p2():
    res = 0
    pos = 50
    for dir, count in OPERATIONS:
        npos = pos + (dir*count)
        if npos <= 0 and pos > 0:
            res += 1
        res += abs(npos) // MOD
        pos = npos % MOD
    print(res)


p1()
p2()

