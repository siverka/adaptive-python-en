a, b, n = [int(input()) for _ in range(3)]
# # a, b, n = 10, 15, 2  # 20 30
# a, b, n = 2, 50, 4  # 10 0
cost = 100 * a * n + b * n
print(cost // 100, cost % 100)
