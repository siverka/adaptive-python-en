def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc)**2 + (y - yc)**2 <= r**2

x, y, xc, yc, r = [float(input()) for _ in range(5)]
print('YES' if IsPointInCircle(x, y, xc, yc, r) else 'NO')
