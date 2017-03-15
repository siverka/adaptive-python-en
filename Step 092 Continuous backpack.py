n, capacity = [int(i) for i in input().split()]
costs = []
for _ in range(n):
    c, w = [int(x) for x in input().split()]
    costs.extend([c/w for _ in range(w)])

costs.sort(reverse=True)
print('{:.3f}'.format(sum(costs[:capacity])))
