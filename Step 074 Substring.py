string, substring = [input() for _ in range(2)]
n = len(substring)
indexes = [i for i in range(len(string) - n + 1) if string[i:i+n] == substring]
if len(indexes) > 0:
    print(*indexes)
else:
    print(-1)
