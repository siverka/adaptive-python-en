import numpy as np

n = int(input())
m = np.array([[int(x) for x in input().split()] for _ in range(n)])
k = int(input())

out = np.diagonal(m, -k)
print(*out)
