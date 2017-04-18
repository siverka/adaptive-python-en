def pow(a, p):
    if p < 0:
        return 1 / pow(a, -p)
    r = 1
    for _ in range(p):
        r *= a
    return r
