n = int(input())
detectors = [int(input()) for _ in range(n)]
counts = [detectors.count(i) for i in [0, 1, -1]]
print(*counts)
