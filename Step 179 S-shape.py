def get_row(i, m):
    if i % 2 == 0:
        return list(range(i * m + 1, (i + 1) * m + 1))
    else:
        return list(range((i + 1) * m, i * m, -1))

n, m = map(int, input().split())
matrix = [get_row(i, m) for i in range(n)]
for row in matrix:
    print(('{:4d}'*len(row)).format(*row))
