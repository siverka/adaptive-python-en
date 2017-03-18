n, m = map(int, input().split())
squares = [list(map(int, input().split())) for _ in range(n)]

i = 0
for j in range(i+1, m):
    squares[i][j] += squares[i][j-1]
for k in range(i+1, n):
    squares[k][i] += squares[k-1][i]

for i in range(1, min(n, m)):
    # corner
    squares[i][i] += min(squares[i-1][i], squares[i][i-1])
    # horizontal
    for j in range(min(i+1, m), m):
        squares[i][j] += min(squares[i-1][j], squares[i][j-1])
    # vertical
    for k in range(min(i+1, n), n):
        squares[k][i] += min(squares[k-1][i], squares[k][i-1])

print(squares[n-1][m-1])
