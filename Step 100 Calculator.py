n = int(input())
f = [0, 1, 1]  # number of steps for [1, 2, 3]
g = [-1, 1, 2]

for m in range(4, n + 1):  # number
    i = m - 1  # index
    steps = [f[i-1] + 1]
    op = [0]
    if m % 2 == 0:
        steps.append(f[m // 2 - 1] + 1)
        op.append(1)
    if m % 3 == 0:
        steps.append(f[m // 3 - 1] + 1)
        op.append(2)
    f.append(min(steps))
    g.append(op[steps.index(f[-1])])

operations = [lambda x: x - 1, lambda x: x // 2, lambda x: x // 3]
inter = []
m = n
while True:
    inter.append(m)
    op = g[m-1]
    if op == -1:
        break
    m = operations[op](m)

print(f[n - 1])
print(*inter[::-1])
