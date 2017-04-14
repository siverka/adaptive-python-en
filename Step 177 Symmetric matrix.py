n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
symmetric = [matrix[i][j] == matrix[j][i] for i in range(n) for j in range(i+1, n)]
print('YES' if all(symmetric) else 'NO')
