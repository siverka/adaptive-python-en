def floor_space(shape):
    if shape == "triangle":
        a, b, c = [float(input()) for _ in range(3)]
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s
    elif shape == "rectangle":
        x, y = [float(input()) for _ in range(2)]
        return x * y
    else:
        r = float(input())
        return 3.14 * (r ** 2)

print(floor_space(input()))
