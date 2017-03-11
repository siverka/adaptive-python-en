from math import trunc

p, x, y = [int(input()) for _ in range(3)]
s = 100 * x + y
s += trunc(s * p / 100)
print(int(s // 100))
print(int(s % 100))

# p, x, y = 1, 1005000000000000, 1
# s = 100 * x + y
# s += trunc(s * p / 100)
# print(int(s // 100))
# print(int(s % 100))
#
# s = (100 * x + y) * (1 + p / 100)
# print(int(s // 100))
# print(int(s % 100))
