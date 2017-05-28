s = input()
t = input()
m = len(t)
sub = [s[i:i + m] == t for i in range(len(s) - m + 1)]
print(sum(sub))
