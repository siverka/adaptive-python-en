def spin(s, n):
    res = [[0 for i in range(n)] for j in range(n)]
    res[0][:] = range(s, s + n)
    res[n-1][:] = range(s + 3*n - 3, s + 2*n - 3, -1)
    for i in range(1, n-1):
        res[i][n-1] = res[i-1][n-1] + 1
    for i in range(n-2, 0, -1):
        res[i][0] = res[i+1][0] + 1
    return res


def filled(big, small):
    m = len(small)
    d = int((len(big) - m) / 2)
    for i in range(m):
        for j in range(m):
            big[i+d][j+d] = small[i][j]
    return big


def start(s, n):
    return s + 4*(n - 1)


def main_spin(s, n):
    res = spin(s, n)
    while n > 2:
        s = start(s, n)
        n -= 2
        inner_spin = spin(s, n)
        res = filled(res, inner_spin)
    return res

n = int(input())
r = main_spin(1, n)
for i in r:
    print(*i)
