def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def div(x, y):
    if y == 0:
        return "Division by 0!"
    return x / y


def mult(x, y):
    return x * y


def mod(x, y):
    if y == 0:
        return "Division by 0!"
    return x % y


def pow(x, y):
    return x ** y


def idiv(x, y):
    if y == 0:
        return "Division by 0!"
    return x // y


operations = {"+": add, "-": sub, "/": div, "*": mult, "mod": mod, "pow": pow, "div": idiv}


a = float(input())
b = float(input())
op = input()

print(operations[op](a, b))
