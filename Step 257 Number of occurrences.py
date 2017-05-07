s = input()
t = input()
n, m = len(s), len(t)
occurrences = [s[i:i+m] == t for i in range(n - m + 1)]
print(sum(occurrences))
