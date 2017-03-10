import math


h, a, b = int(input()), int(input()), int(input())
d = math.ceil((h - a) / (a - b)) + 1
print(d)
