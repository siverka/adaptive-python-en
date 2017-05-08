# https://toster.ru/q/239925
# n, m = map(int, input().split())
n, m = 60282445765134413, 2263  # 974
fibs = [1, 1]

for _ in range(2, n):
    fibs.append(sum(fibs[-2:]) % m)

print(fibs[-1])
