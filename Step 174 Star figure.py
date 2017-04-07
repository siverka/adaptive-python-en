def star(i, j, n):
    m = n - 1
    if i == j or i == m / 2 or j == m / 2 or i == m - j:
        return '*'
    else:
        return '.'

n = int(input())
figure = [[star(i, j, n) for j in range(n)] for i in range(n)]
for row in figure:
    print(*row)
