n = int(input())
d = {"North": 0, "West": 0,  "South": 0, "East": 0}
for _ in range(n):
    direction, distance = input().split()
    d[direction] += int(distance)
print(d['East'] - d['West'], d['North'] - d['South'])
