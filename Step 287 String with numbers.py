line = input().split()
result = [int(n) for n in line if n.isdigit()]
print(sum(result))
