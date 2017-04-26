def IsPointInSquare(x, y):
    return abs(y + x) <= 1 and abs(y - x) <= 1

x1, y1 = [float(input()) for _ in range(2)]
print('YES' if IsPointInSquare(x1, y1) else 'NO')
