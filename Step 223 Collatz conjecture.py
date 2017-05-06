def collatz(n):
    seq = [n]
    x = n
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        seq.append(x)
    return seq

print(*collatz(int(input())))
