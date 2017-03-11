sides = [int(input()) for _ in range(3)]
p = sum(sides)
print('YES' if all([2*s < p for s in sides]) else 'NO')
