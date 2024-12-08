

with open("day2.in", "r") as fin:
    REPORTS = [[int(lvl) for lvl in l.split()] for l in fin.readlines()]

def p1(reports: list[list[int]]):
    bounds = (1,2,3)
    ans = 0
    for report in reports:
        prev = report[0]
        pdelt = 0
        safe = 1 
        for i in range(1, len(report)):
            nxt = report[i] - prev
            if abs(nxt) not in bounds or ((pdelt > 0 and nxt < 0) or (pdelt < 0 and nxt > 0)):
                safe = 0 
                break
            prev = report[i] 
            pdelt = nxt
        ans += safe
    print(ans)

def is_safe(report):
    bounds = (1,2,3)
    prev = report[0]
    pdelt = 0
    for i in range(1, len(report)):
        nxt = report[i] - prev
        if abs(nxt) not in bounds or ((pdelt > 0 and nxt < 0) or (pdelt < 0 and nxt > 0)):
            return False
        prev = report[i] 
        pdelt = nxt
    return True

def p2help(report):
    safe = False
    for i in range(len(report)):
        safe = safe or is_safe(report[:i] + report[i+1:])
    return safe


def p2(reports: list[list[int]]):
    ans = 0
    for report in reports:
        ans += 1 if p2help(report) else 0
    print(ans)


p1(REPORTS)
p2(REPORTS)

print(p2help([1,3,9,5,7]))
print(p2help([1,3,0,-2]))
print(p2help([1,4,2,1]))
