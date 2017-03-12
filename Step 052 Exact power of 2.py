from math import log2, modf
n = int(input())
print('YES' if modf(log2(n))[0] == 0 else 'NO')
