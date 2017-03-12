p, x, y, k = [int(input()) for _ in range(4)]
# p, x, y, k = 12, 179, 0, 5  # 315, 43

s = 100 * x + y
for _ in range(k):
    s = int(s * (1 + p / 100))
print(int(s // 100), int(s % 100))
