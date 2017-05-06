from functools import reduce


def f(x):
    if x == 0:
        return 1
    else:
        parts = [i for i in range(x, 0, -2)]
        return reduce(lambda y, z: y * z, parts)
