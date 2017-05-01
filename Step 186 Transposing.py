n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
transpose = [[matrix[i][j] for i in range(n)]for j in range(m)]
for row in transpose:
    print(*row)
