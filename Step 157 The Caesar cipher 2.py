def unicode_cipher(n: int, line: str):
    alpha = range(128512, 128592)
    ans = [chr(alpha[(alpha.index(ord(w)) + n) % 80]) for w in line]
    return ''.join(ans)

print('Result: "%s"' % unicode_cipher(int(input()), input().strip()))
