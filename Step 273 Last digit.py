n = int(input())
fibs = [1, 1]
for _ in range(2, n):
    a = sum(fibs) % 10
    fibs[:] = [fibs[1], a]
print(fibs[-1])
