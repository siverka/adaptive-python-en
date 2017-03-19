# n = int(input())
n = 96234
# n = 5
# n = 3
# n = 2
# n = 1
f = [0, 1, 1]  # number of steps for [1, 2, 3]
g = [1, 2]


for m in range(4, n + 1):  # number
    i = m - 1  # index
    # print('m', m, 'i', i)
    steps = [f[i-1] + 1]
    op = [0]
    if m % 2 == 0:
        steps.append(f[m // 2 - 1] + 1)
        op.append(1)
    if m % 3 == 0:
        steps.append(f[m // 3 - 1] + 1)
        op.append(2)
    # print('steps', steps)
    # print('op', op)
    f.append(min(steps))
    g.append(op[steps.index(f[-1])])

# print('results')
# print(f)
# print('num of steps:', f[-1])
# print(g)
# print('----------------')

operations = [lambda x: x - 1, lambda x: x // 2, lambda x: x // 3]
inter = []
k = n - 2
m = n
while m >= 1:
    # print('n', n, 'k', k)
    inter.append(m)
    m = operations[g[k]](m)
    k = operations[g[k]](k)
    # print(inter)
    # print('op:', g[k])
    # print('new n', n)

# if n == 1:
#     print(0)
# else:
#     print(f[-1])
# print(*inter[::-1])
print(f[-1])
print(len(inter))
