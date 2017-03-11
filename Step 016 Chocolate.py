n, m, k = [int(input()) for _ in range(3)]
print('YES' if k <= n * m and (k % n == 0 or k % m == 0) else 'NO')
