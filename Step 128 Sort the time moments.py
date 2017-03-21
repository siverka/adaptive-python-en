n = int(input())
times = [[int(i) for i in input().split()] for _ in range(n)]
times.sort()
for time in times:
    print(*time)
