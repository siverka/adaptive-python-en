n, m = (int(i) for i in input().split())
field = [list(input()) for _ in range(n)]
answer = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if field[i][j] == '*':
            answer[i][j] = '*'
        else:
            for k in [e for e in [i-1, i, i+1] if 0 <= e < n]:
                for l in [e for e in [j-1, j, j+1] if 0 <= e < m]:
                    if k == i and l == j:
                        continue
                    if field[k][l] == '*':
                        answer[i][j] += 1

for e in answer:
    print(''.join([str(i) for i in e]))
