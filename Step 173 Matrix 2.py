n = int(input())
matrix = [[abs(i-j) for j in range(n)] for i in range(n)]
for row in matrix:
    print(*row)
