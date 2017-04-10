def cipher(n: int, line: str):
    alpha = ' abcdefghijklmnopqrstuvwxyz'
    ans = [alpha[(alpha.index(w) + n) % len(alpha)] for w in line]
    return ''.join(ans)

print('Result: "%s"' % cipher(int(input()), input().strip()))
