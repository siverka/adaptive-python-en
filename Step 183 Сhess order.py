n, m = map(int, input().split())

matrix = [[0 for _ in range(m)] for _ in range(n)]
last = 1
for i in range(n):
    stop = m // 2
    if i % 2 == 0 and m % 2 != 0:
        stop += 1
    matrix[i][(i % 2)::2] = list(range(last, last + stop))
    last += stop

for row in matrix:
    print(('{:4d}'*m).format(*row))
