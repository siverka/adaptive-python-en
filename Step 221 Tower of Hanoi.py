def move(indxs: list):
    lens = [len(pegs[i]) == 0 for i in indxs]
    if any(lens):
        l = indxs[lens.index(True)]  # 0
        k = indxs[lens.index(False)]  # not 0
    else:
        vals = [pegs[i][-1] for i in indxs]
        l = [i for i in indxs if pegs[i][-1] == max(vals)][0]
        k = [i for i in indxs if pegs[i][-1] == min(vals)][0]
    pegs[l].append(pegs[k].pop())
    print(k+1, '-', l+1)


n = int(input())
pegs = [[i for i in range(n, 0, -1)], [], []]

if n % 2 == 0:
    steps = [[0, 1], [0, 2], [1, 2]]
else:
    steps = [[0, 2], [0, 1], [1, 2]]

while len(pegs[-1]) != n:
    for s in steps:
        if len(pegs[-1]) != n:
            move(s)

