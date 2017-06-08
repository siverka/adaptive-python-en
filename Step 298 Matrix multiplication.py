import numpy as np

n = int(input())
a = np.array([[int(x) for x in input().split()] for _ in range(n)])
b = np.array([[int(x) for x in input().split()] for _ in range(n)])

for row in a.dot(b):
    print(*row)
