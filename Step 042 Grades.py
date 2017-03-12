n = int(input())
grades = [int(input()) for _ in range(n)]
counts = [grades.count(i) for i in range(2, 6)]
print(*counts)
