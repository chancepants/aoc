with open("day3.in", "r") as fin:
    BATTERIES = [[int(b) for b in line.strip()] for line  in fin.readlines()]

def p1():
    sm = 0
    for bat in BATTERIES:
        mx = 0
        pos = -1
        for i in range(len(bat)-1):
            if bat[i] > mx:
                mx = bat[i]
                pos = i
        lsb = max(bat[pos+1:])
        sm += int(str(f"{mx}{lsb}"))
    print(sm)


def p2():
    def find_mx(i: int, j: int, bat: list[int]) -> tuple[int, int]:
        mx = 0
        pos = -1
        # print(i,j)
        for i in range(i,j):
            if bat[i] > mx:
                mx = bat[i]
                pos = i
        return mx,pos

    sm = 0
    for bat in BATTERIES:
        l = -1
        dig_lst: list[str] = []
        for k in range(11,-1, -1):
            dig, l = find_mx(i=l+1, j=len(bat)-k, bat=bat)
            dig_lst.append(str(dig))
        # print("".join(dig_lst))
        sm += int("".join(dig_lst))
    print(sm)

p1()
p2()
