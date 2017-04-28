import turtle


def koch_turns(n):
    angles = [60, -120, 60]
    if n == 1:
        return angles
    else:
        kch = koch_turns(n-1)
        res = []
        for i in range(7):
            if i % 2 == 0:
                res.extend(kch)
            else:
                res.append(angles[(i - 1) // 2])
        return res


def koch_curve(n, line_length=10):
    for move in koch_turns(n):
        turtle.forward(line_length)
        turtle.left(move)
    turtle.forward(line_length)
    turtle.exitonclick()


koch = koch_turns(int(input()))
for turn in koch:
    print('turn', turn)
koch_curve(3)
