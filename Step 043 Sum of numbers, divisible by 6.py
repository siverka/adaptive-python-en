n = int(input())
numbers = [int(input()) for _ in range(n)]
print(sum(i for i in numbers if i % 6 == 0))
