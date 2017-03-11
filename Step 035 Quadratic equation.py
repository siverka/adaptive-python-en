from math import sqrt


a, b, c = [float(input()) for _ in range(3)]
d = b ** 2 - 4 * a * c
if d == 0:
    print(-b / 2 / a)
elif d > 0:
    roots = [(-b + sqrt(d)) / 2 / a, (-b - sqrt(d)) / 2 / a]
    roots.sort()
    print(*roots)
