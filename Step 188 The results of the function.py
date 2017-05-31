n = int(input())
values = {}

for _ in range(n):
    x = int(input())
    if x not in values:
        values[x] = f(x)
    print(values[x])
