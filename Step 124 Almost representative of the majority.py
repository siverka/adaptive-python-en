n = int(input())
array = [int(i) for i in input().split()]
repeats = [array.count(a) for a in set(array)]
answer = any(map(lambda r: r > n / 3, repeats))
print(int(answer))
