import numpy as np

n, m, *numbers = [int(x) for x in input().split()]
mtrx = np.fromiter(numbers, np.int).reshape((n, m))
print(*mtrx.T.flatten())
