def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1

point = [float(input()) for _ in range(2)]
print('YES' if IsPointInSquare(*point) else 'NO')
