lst = [int(x) for x in input().split()]
n = len(lst)
if n > 1:
    answer = [lst[(i-1) % n] + lst[(i+1) % n] for i in range(n)]
else:
    answer = lst
print(*answer)
