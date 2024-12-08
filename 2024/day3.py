import re
import bisect

# with open("day3.example", "r") as fin:
with open("day3.in", "r") as fin:
    TXT = fin.read()


def p1(txt):
    rgx = r"mul\([0-9]*,[0-9]*\)"
    ans = 0
    for mtch in re.findall(rgx, txt):
        s = mtch[4:-1]
        nums = s.split(",")
        ans += (int(nums[0]) * int(nums[1]))
    print(ans)


def p2(txt):
    rgx = r"mul\([0-9]*,[0-9]*\)"
    dorgx = r"do\(\)"
    dontrgx = r"don't\(\)"
    donts = []
    dos = []
    ans = 0
    for mtch in re.finditer(dontrgx, txt):
        donts.append(mtch.end())
    for mtch in re.finditer(dorgx, txt):
        dos.append(mtch.end())
    for mtch in re.finditer(rgx, txt):
        prev_dont = bisect.bisect_right(donts, mtch.start())
        prev_do = bisect.bisect_right(dos, mtch.start())
        pdont = -1 if not prev_dont else donts[prev_dont-1]
        pdo = 0 if not prev_do else dos[prev_do-1]
        if pdo > pdont:
            s = txt[mtch.start()+4:mtch.end()-1]
            nums = s.split(",")
            # print(nums, mtch.start(), prev_dont, donts[prev_dont], prev_do, dos[prev_do])
            ans += (int(nums[0]) * int(nums[1]))
    print(ans)

p1(TXT)
p2(TXT)
