m = []
line = input()
while line != 'end':
    m.append([int(x) for x in line.split()])
    line = input()

n, l = len(m), len(m[0])

swapped = [[m[(i-1) % n][j] + m[(i+1) % n][j] +
            m[i][(j-1) % l] + m[i][(j+1) % l]
            for j in range(l)]for i in range(n)]

for row in swapped:
    print(*row)
