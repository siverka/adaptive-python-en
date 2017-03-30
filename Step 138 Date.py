from datetime import date, timedelta

year, month, day = map(int, input().split())
answer = date(year, month, day) + timedelta(days=int(input()))
print(answer.year, answer.month, answer.day)
