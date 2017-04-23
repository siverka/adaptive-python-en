n, m = map(int, input().split())
intervals = [[int(x) for x in input().split()]for _ in range(n)]
points = [int(x) for x in input().split()]
counts = [0 for _ in range(m)]

intervals.sort(key=lambda interval: interval[0])
points = list(zip(points, range(m)))
points.sort(key=lambda point: point[0])


for i in range(m):
    j = 0
    while j < n and intervals[j][0] <= points[i][0]:
        if points[i][0] <= intervals[j][1]:
            counts[i] += 1
        j += 1

print(*counts)
