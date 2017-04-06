n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
maximum = max(max(matrix, key=lambda r: max(r)))

for i in range(n):
    if maximum in matrix[i]:
        print(i, matrix[i].index(maximum))
        break
