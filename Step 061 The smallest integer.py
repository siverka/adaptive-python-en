from math import factorial

m = int(input())
n = 1
while factorial(n) <= m:
    n += 1
print(n)
