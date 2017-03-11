from functools import reduce


def heron(sides):
    p = sum(sides) / 2
    s = p * reduce(lambda x, y: x * y, [p - i for i in sides])
    return s ** 0.5

print(heron([int(input()) for _ in range(3)]))
