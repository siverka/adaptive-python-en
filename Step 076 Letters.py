def letters(s, a, b):
    if s.count(a) == 0:
        return 0
    if a in b:
        return 'Impossible'
    count = 0
    while a in s:
        s = s.replace(a, b)
        count += 1
    return count

s, a, b = (input() for _ in range(3))
print(letters(s, a, b))
