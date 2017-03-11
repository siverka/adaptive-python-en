n, m, x, y = [int(input()) for _ in range(4)]

d = min(x, min(n, m) - x, y, max(n, m) - y)
print(d)
