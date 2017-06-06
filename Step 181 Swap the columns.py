import numpy as np

n, m = map(int, input().split())
mtrx = np.array([[int(x) for x in input().split()] for _ in range(n)])
a1, a2 = map(int, input().split())
mtrx[:, [a2, a1]] = mtrx[:, [a1, a2]]
for row in mtrx:
    print(*row)
