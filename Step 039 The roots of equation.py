def f(x, coef):
    return coef[0] * x ** 3 + coef[1] * x ** 2 + coef[2] * x + coef[3]

coeff = [int(input()) for _ in range(4)]
for i in range(1001):
    if f(i, coeff) == 0:
        print(i)

# coeff = [-1, 1, -1, 1]  # 1
# coeff = [1, 1, 1, 1]  # none
# coeff = [0, 1, -6, 5]  # 1 5
