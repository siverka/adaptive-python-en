n, m = map(int, input().split())
numbers = [i // 2 + 1 if i % 2 == 0 else 0 for i in range(n*m)]
matrix = [numbers[i:i+m] for i in range(0, n*m, m)]
for row in matrix:
    print(('{:4d}'*m).format(*row))
