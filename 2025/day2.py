with open("day2.in", "r") as fin:
    lines = fin.readlines()
    _ranges = lines[0].strip().split(",")
    RANGES = [[r for r in _range.split("-")] for _range in _ranges]


def p1():
    def solve(lower: int, upper: int) -> int:
        res = 0
        cur = str(lower)
        lbound = int(f"1{'0' * (len(cur)//2 - 1)}")
        rbound = int("9"*(len(str(upper))//2))
        for i in range(lbound, rbound+1):
            opt = int(str(f"{i}{i}"))
            if opt >= lower and opt <= upper:
                print(opt)
                res += opt
        return res

    sm = 0
    for l,r in RANGES:
        if not len(l) % 2 or not len(r) % 2:
            sm += solve(int(l) if not len(l) % 2 else int(f"1{'0'*(len(r)-1)}"), int(r) if not len(r) % 2 else int("9"*len(l)))

    print(sm)

def p2():
    st = set()
    def solve(chunk_size: int, num_chunks: int, lower: int, upper: int) -> None:
        for i in range(int(f"1{'0'*(chunk_size-1)}"), int("9"*chunk_size)+1):
            opt = int(str(i)*num_chunks)
            if opt >= lower and opt <= upper:
                # print(opt)
                st.add(opt)

    for l,r in RANGES:
        for i in range(len(l), len(r)+1):
            for j in range(2, i+1):
                if not i % j:
                    solve(chunk_size=i//j, num_chunks=j, lower=int(l), upper=int(r))
    print(sum(st))

# p1()
p2()

