n = int(input())
points = [[int(x) for x in input().split()] for _ in range(n)]
points.sort(key=lambda point: point[0]**2 + point[1]**2)
for point in points:
    print(*point)
