n = int(input())
participants = [[int(x) for x in input().split()]for _ in range(n)]

participants.sort(key=lambda x: x[0])
participants.sort(key=lambda x: x[1], reverse=True)
for p in participants:
    print(*p)
