n = int(input())
items = input().split()
for i in range(n // 2):
    items[2*i], items[2*i+1] = items[2*i+1], items[2*i]
print(*items)
