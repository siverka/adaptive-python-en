numbers = [int(input()) for _ in range(int(input()))]
print(max(i for i in numbers if i % 4 == 0))
