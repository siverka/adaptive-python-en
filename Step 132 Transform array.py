import numpy as np
mat = 2 * np.eye(3, 4) + np.eye(3, 4, k=1)
print(mat.reshape((mat.size, 1)))
