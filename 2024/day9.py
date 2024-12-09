with open("day9.in", "r") as fin:
    # with open("day9.example", "r") as fin:
    line = fin.readline().strip()


def p1(disk: str):
    expanded = []
    for i in range(len(disk)):
        if i % 2:
            expanded.extend(int(disk[i]) * ".")
        else:
            expanded.extend([str(i // 2) for _ in range(int(disk[i]))])
    l, r = 0, len(expanded) - 1
    # find first block of open space and count how big it is
    # find first file-block to move from the end
    # if it fits put it in
    while l < r:
        while expanded[l] != ".":
            l += 1
        while expanded[r] == ".":
            r -= 1
        if l > r:
            break
        # print(l,r, expanded[l], expanded[r])
        expanded[l], expanded[r] = expanded[r], expanded[l]
    # print("".join(expanded))
    ans = 0
    for i, c in enumerate(expanded):
        if c == ".":
            break
        ans += i * int(c)
    print(ans)


def next_file(expanded: list[str], r: int, processed: set[str]):
    while r > 0 and (expanded[r] == "." or expanded[r] in processed):
        r -= 1
    if r < 0:
        return None
    end = r
    fid = expanded[r]
    # print("".join(expanded))
    # print(fid)
    while r >= 0 and expanded[r] == fid:
        r -= 1
    return r + 1, end, fid


def next_free_chunk(expanded: list[str], l):
    while l < len(expanded) and expanded[l] != ".":
        l += 1
    if l == len(expanded):
        return None
    start = l
    while l < len(expanded) and expanded[l] == ".":
        l += 1
    return start, l - 1


def p2(disk: str):
    expanded = []
    for i in range(len(disk)):
        if i % 2:
            expanded.extend(int(disk[i]) * ".")
        else:
            expanded.extend([str(i // 2) for _ in range(int(disk[i]))])
    r = len(expanded) - 1
    processed = set()
    file = next_file(expanded, r, processed)
    while file is not None:
        fs, fe, fid = file
        chunk = next_free_chunk(expanded, 0)
        while chunk is not None:
            cs, ce = chunk
            # print((fs,fe), (cs,ce))
            if cs > fe:
                break
            if ce - cs >= fe - fs:
                sz = fe + 1 - fs
                expanded[cs : cs + sz], expanded[fs : fe + 1] = (
                    expanded[fs : fe + 1],
                    expanded[cs : cs + sz],
                )
                break
            else:
                chunk = next_free_chunk(expanded, ce + 1)
        processed.add(fid)
        file = next_file(expanded, fs - 1, processed)

    ans = 0
    for i, c in enumerate(expanded):
        if c != ".":
            ans += i * int(c)
    print(ans)


p1(line)
p2(line)
