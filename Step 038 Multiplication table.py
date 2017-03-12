a, b, c, d = [int(input()) for _ in range(4)]
# a, b, c, d = 7, 10, 5, 6
# a, b, c, d = 5, 5, 6, 6
# a, b, c, d = 1, 3, 2, 4

print('', *range(c, d + 1), sep='\t')
for i in range(a, b + 1):
    print(i, *[i * j for j in range(c, d + 1)], sep='\t')
