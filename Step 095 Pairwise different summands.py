n = int(input())

i = 1
summands = []
while n >= i:
    summands.append(i)
    n -= i
    i += 1
if n > 0:
    summands[-1] += n

print(len(summands))
print(*summands)
