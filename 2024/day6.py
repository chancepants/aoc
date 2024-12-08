import copy

GRID = []
with open("day6.in", "r") as fin:
# with open("day6.example", "r") as fin:
    lines = [line.strip() for line in fin.readlines()]
    for line in lines:
        GRID.append([c for c in line])

# print(GRID)


def start(grid: list[list[str]]) -> tuple[int,int]:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                return i,j
    raise ValueError("start not found") 


def p1(grid: list[list[str]]):
    pos = set()
    r,c = start(grid)
    dirs = [(-1,0), (0, 1), (1, 0), (0, -1)]
    di = 0
    while r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r]):
        pos.add((r,c))
        dr,dc = dirs[di]
        nr = r + dr
        nc = c + dc
        while nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[nr]) and grid[nr][nc] == "#":
            di = (di + 1) % len(dirs)
            dr,dc = dirs[di]
            nr = r + dr
            nc = c + dc
        r = nr
        c = nc
    print(len(pos))

def print_g(grid: list[list[str]], pos: set[tuple[int,int,int]], nnr, nnc) -> None:
    g = copy.deepcopy(grid)
    for r in range(len(g)):
        for c in range(len(g[r])):
            for i in range(4):
                if (r,c,i) in pos and g[r][c] != "^":
                    g[r][c] = "Z"
    g[nnr][nnc] = "X"
    for row in g:
        print("".join(row))

def walk(grid: list[list[str]], r: int, c: int, di: int, pos: set, nnr, nnc) -> bool:
    sr,sc,sdi = r,c,di
    dirs = [(-1,0), (0, 1), (1, 0), (0, -1)]
    while r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r]):
        if (r,c,di) in pos:
            # print_g(grid, pos, nnr, nnc)
            # print((sr,sc, sdi), (r,c,di))
            return True
        pos.add((r,c,di))
        dr,dc = dirs[di]
        nr = r + dr
        nc = c + dc
        while nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[nr]) and grid[nr][nc] == "#":
            di = (di + 1) % len(dirs)
            dr,dc = dirs[di]
            nr = r + dr
            nc = c + dc
        r = nr
        c = nc
    return False

def p2(grid: list[list[str]]):
    sr,sc = start(grid)
    blocks = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                grid[i][j] = "#"
                if walk(grid, sr, sc, 0, set(), 0, 0):
                    blocks.add((i,j))
                grid[i][j] = "."
    print(len(blocks))


# def p2(grid: list[list[str]]):
    # pos = set()
    # prev = set()
    # blocks = set()
    # r,c = start(grid)
    # sr,sc = r,c
    # dirs = [(-1,0), (0, 1), (1, 0), (0, -1)]
    # di = 0
    #
    # while r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r]):
    #     pos.add((r,c,di))
    #     prev.add((r,c))
    #     # if grid[r][c] == ".":
    #     #     grid[r][c] = "Z"
    #     dr,dc = dirs[di]
    #     nr = r + dr
    #     nc = c + dc
    #     while nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[nr]) and grid[nr][nc] == "#":
    #         di = (di + 1) % len(dirs)
    #         dr,dc = dirs[di]
    #         nr = r + dr
    #         nc = c + dc
    #     if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[nr]) and (nr,nc) not in blocks:
    #         ddi = (di + 1) % len(dirs)
    #         ddr,ddc = dirs[ddi]
    #         grid[nr][nc] = "#"
    #         if walk(grid, r+ddr, c+ddc, ddi, copy.copy(pos), nr,nc) and (nr,nc) != (sr,sc):
    #             blocks.add((nr,nc))
    #             # grid[nr][nc] = "X"
    #         grid[nr][nc] = "."
    #         # if (r+dr,c+dc,ddi) in pos:
    #         #     print((r,c), (r+dr,c+dc))
    #         #     blocks.add((nr,nc))
    #         #     grid[nr][nc] = "X"
    #     r = nr
    #     c = nc
    # print(len(blocks))
    # print((sr,sc))
    # # print(blocks)
    # # for row in grid:
    # #     print("".join(row))

p1(GRID)
p2(GRID)
