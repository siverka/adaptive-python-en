from math import factorial as f
n, k = map(int, input().split())
print(int(f(n)/f(k)/f(n-k)))
