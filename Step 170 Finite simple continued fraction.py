m, n = map(int, input().split('/'))
i = int(m/n)
fractions = [i]
while m % n != 0:
    m = m - n * i
    m, n = n, m
    i = int(m/n)
    fractions.append(i)
print(*fractions)
